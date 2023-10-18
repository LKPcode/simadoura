import os
import re
import requests

def download_images_from_local_css_file(css_file_path, base_url):
    # Check if the CSS file exists
    if not os.path.exists(css_file_path):
        print("The provided CSS file does not exist.")
        return

    # Read the CSS file
    with open(css_file_path, 'r') as f:
        css_content = f.read()

    # Extract URLs from CSS using a regex
    img_urls = re.findall(r'url\(["\']?(.+?)["\']?\)', css_content)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Create directory if doesn't exist
    if not os.path.exists('imges'):
        os.makedirs('imges')

    for img_url in img_urls:
        # Make URL absolute if it's relative
        if not img_url.startswith(('http:', 'https:', '//')):
            img_url = os.path.join(base_url, img_url)
        img_name = os.path.basename(img_url)

        # Download the image
        with requests.get(img_url, stream=True, headers=headers) as r:
            r.raise_for_status()
            with open(os.path.join('imges', img_name), 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

    print("Images downloaded successfully!")

if __name__ == "__main__":
    css_file_path = input("Enter the path to the local CSS file: ")
    base_url = input("Enter the base URL (e.g., https://example.com): ")
    download_images_from_local_css_file(css_file_path, base_url)
