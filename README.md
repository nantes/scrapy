# Web Scraper

A simple web application that allows users to enter a URL, scrape its HTML content, and download it as an HTML file.

## Features

- Enter a URL in a web form.
- Scrapes the full HTML content of the provided URL.
- Provides a download link for the scraped HTML file.
- Basic error handling for URL fetching issues.

## Project Structure

```
/
|-- main.py             # Flask application
|-- requirements.txt    # Python dependencies
|-- templates/
|   |-- index.html      # Main HTML page for the UI
|-- static/
|   |-- script.js       # Client-side JavaScript
|   |-- style.css       # CSS for styling
|-- downloads/          # Temporary directory for scraped files (created automatically)
|-- README.md           # This file
```

## Setup and Installation

1.  **Clone the repository (if applicable) or download the files.**

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

1.  **Ensure you are in the project's root directory and your virtual environment is activated.**
2.  **Run the Flask application:**
    ```bash
    python main.py
    ```
3.  **Open your web browser and go to:**
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## How to Use

1.  Once the application is running, open the URL [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.
2.  Enter the full URL of the website you want to scrape into the input field (e.g., `https://example.com`).
3.  Click the "Scrape" button.
4.  If successful, a download link for the scraped HTML file will appear. Click it to download the file.
5.  If there's an error (e.g., invalid URL, website not reachable), an error message will be displayed.

## Dependencies

- Flask
- Requests
- BeautifulSoup4
