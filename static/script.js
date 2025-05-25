document.addEventListener('DOMContentLoaded', function() {
    const scrapeForm = document.getElementById('scrapeForm');
    const urlInput = document.getElementById('urlInput');
    const resultDiv = document.getElementById('result');

    scrapeForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const urlValue = urlInput.value;
        resultDiv.innerHTML = ''; // Clear previous messages
        resultDiv.textContent = 'Scraping...';

        fetch('/scrape', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({url: urlValue})
        })
        .then(response => {
            if (response.ok) {
                return response.json().then(data => {
                    if (data.download_url) {
                        const a = document.createElement('a');
                        a.href = data.download_url;
                        a.textContent = 'Download Scraped File';
                        a.target = '_blank';
                        resultDiv.innerHTML = ''; // Clear "Scraping..."
                        resultDiv.appendChild(a);
                    } else if (data.error) {
                        resultDiv.textContent = 'Error: ' + data.error;
                        resultDiv.classList.add('error'); 
                    }
                });
            } else {
                return response.json().then(errData => {
                    resultDiv.textContent = 'Error: ' + (errData.error || response.statusText);
                    resultDiv.classList.add('error');
                });
            }
        })
        .catch(error => {
            resultDiv.textContent = 'Request failed: ' + error;
            resultDiv.classList.add('error');
        });
    });
});
