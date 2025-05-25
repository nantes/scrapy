import os
import uuid
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, send_from_directory, jsonify

app = Flask(__name__)

# Ensure the downloads directory exists
os.makedirs('downloads', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)
    except requests.exceptions.Timeout:
        return jsonify({"error": f"Could not fetch URL: Request timed out after 10 seconds"}), 400
    except requests.exceptions.HTTPError as e:
        return jsonify({"error": f"URL returned status: {e.response.status_code}"}), 400
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Could not fetch URL: {str(e)}"}), 400

    # Create a unique filename for the scraped content
    filename = f"{uuid.uuid4().hex}.html"
    filepath = os.path.join('downloads', filename)

    try:
        # Save the fetched HTML content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(response.text)
    except IOError as e:
        return jsonify({"error": f"Could not save scraped file: {str(e)}"}), 500


    return jsonify({"download_url": f"/download/{filename}"})

@app.route('/download/<filename>')
def download_file(filename):
    # Secure the filename
    safe_filename = os.path.basename(filename)
    if not safe_filename or '..' in safe_filename or '/' in safe_filename:
        return jsonify({"error": "Invalid filename"}), 400
    
    directory = os.path.abspath('downloads') # Use absolute path for send_from_directory
    
    # Check if file exists before attempting to send
    if not os.path.exists(os.path.join(directory, safe_filename)):
        return jsonify({"error": "File not found"}), 404

    try:
        return send_from_directory(directory, safe_filename, as_attachment=True)
    except Exception as e:
        # Log the error for debugging
        app.logger.error(f"Error sending file {safe_filename}: {str(e)}")
        return jsonify({"error": "Could not send file"}), 500

if __name__ == '__main__':
    app.run(debug=True)
