# URL Shortener Service with Click Analytics

This is a simple Flask-based web service that generates shortened URLs and tracks click analytics for each URL.

### Features

*   One-click shortening of original URLs
*   Detailed analytics for each shortened URL, including clicks and timestamp
*   SQLite database to store URLs and analytics

### Setup/Run Instructions

1.  Clone the repository: `git clone https://github.com/[your-username]/url-shorter-service.git`
2.  Install dependencies: `pip install -r requirements.txt`
3.  Run the service: `python app.py`
4.  Use a tool like Postman or cURL to send POST requests to `/shorten` with your original URL in JSON format.

    Example request body:

    {
    "url": "https://www.example.com"
}

5.  Send GET requests to `http://localhost:5000/<id>/click` to simulate clicks on shortened URLs, and view analytics for each ID.

### Sample Output

Shortened URL:
{
    "original_url": "https://www.example.com",
    "shortened_url": "http://localhost:5000/12345"
}

Click Analytics:
{
    "original_url": "https://www.example.com",
    "shortened_url": "http://localhost:5000/12345",
    "clicks": 1,
    "last_clicked": 1643723900.234567
}

### What I learned

I built this URL shortener service to gain hands-on experience with Flask, SQLite databases, and click analytics tracking. This project taught me the importance of proper error handling, data validation, and database management in a real-world application.