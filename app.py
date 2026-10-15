import sqlite3
from flask import Flask, request, jsonify
from uuid import uuid4
import time

app = Flask(__name__)
db = sqlite3.connect('urls.db')
cursor = db.cursor()

# Create table for URLs and analytics
cursor.execute('''
    CREATE TABLE IF NOT EXISTS urls (
        id TEXT PRIMARY KEY,
        original_url TEXT NOT NULL,
        clicks INTEGER DEFAULT 0,
        last_clicked REAL DEFAULT CURRENT_TIMESTAMP
    )
''')

@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    if 'url' not in data:
        return jsonify({'error': 'URL missing'}), 400
    
    original_url = data['url']
    
    # Generate unique ID and store URL in database
    cursor.execute('INSERT INTO urls (id, original_url) VALUES (?, ?)', (str(uuid4()), original_url))
    db.commit()
    url_id = cursor.lastrowid
    
    # Return shortened URL and analytics info
    shortened_url = f'http://localhost:5000/{url_id}'
    click_analytics = {
        'original_url': original_url,
        'shortened_url': shortened_url,
        'clicks': 1,
        'last_clicked': time.time()
    }
    
    return jsonify(click_analytics), 201

@app.route('/<id>/click', methods=['POST'])
def click(id):
    cursor.execute('SELECT * FROM urls WHERE id=?', (id,))
    url_data = cursor.fetchone()
    
    if not url_data:
        return jsonify({'error': 'URL not found'}), 404
    
    original_url, shortened_url, clicks, last_clicked = url_data
    new_clicks = clicks + 1
    new_last_clicked = time.time()
    
    # Update analytics in database
    cursor.execute('UPDATE urls SET clicks=?, last_clicked=? WHERE id=?', (new_clicks, new_last_clicked, id))
    db.commit()
    
    return jsonify({'message': 'URL clicked successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)