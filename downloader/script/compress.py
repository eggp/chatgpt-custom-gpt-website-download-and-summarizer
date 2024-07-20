import os
import subprocess

# Get the website URL from environment variable
website_url = os.getenv('WEBSITE_URL')
# download_dir = "/app/downloaded_site"
download_dir = os.getenv('DOWNLOAD_DIRECTORY')

# Function to download the website using HTTrack
def download_website(url, directory):
    # Added --stay-on-same-address flag to ensure only the same domain is downloaded
    subprocess.run(["httrack", url, "-O", directory, "+*.html", "-rN", "-s0", "-%v", "--stay-on-same-address"], check=True)

# Download the website
try:
    download_website(website_url, download_dir)
except subprocess.CalledProcessError as e:
    print(f"Error during website download: {e}")
    exit(1)
