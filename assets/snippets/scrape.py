import os
import requests
from bs4 import BeautifulSoup

# Function to download an image
def download_image(url, folder):
    try:
        # Send a GET request to the image URL
        response = requests.get(url)
        # Get the image file name from the URL
        img_name = os.path.join(folder, url.split("/")[-1])
        # Write the image to the folder
        with open(img_name, 'wb') as file:
            file.write(response.content)
        print(f"Image saved as {img_name}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

# Function to scrape images from a webpage
def scrape_images(url, folder):
    try:
        # Make the directory to store images if it doesn't exist
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Send a GET request to the webpage
        response = requests.get(url)
        # Parse the content of the webpage using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all image tags on the webpage
        img_tags = soup.find_all('img')
        # Extract the image URLs
        img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]

        # Loop through the image URLs and download them
        for img_url in img_urls:
            if img_url.startswith('http'):
                download_image(img_url, folder)
            else:
                # Handle relative URLs
                full_url = url + img_url if img_url.startswith('/') else url + '/' + img_url
                download_image(full_url, folder)
    
    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")

# URL of the page to scrape
page_url = 'https://www.slavery.amdigital.co.uk/visual-resources/gallery' # Replace with your target URL
# Folder to store images
folder_name = 'GitHub'

# Call the function to start scraping images
scrape_images(page_url, folder_name)