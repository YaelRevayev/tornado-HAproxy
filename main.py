import os
import requests
import logging

def send_images(directory, url):
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # Create an empty list to hold the files
    files_list = []

    # Iterate over the files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            # Open the file and prepare it for upload
            with open(filepath, 'rb') as file:
                # Add the file to the list of files
                files_list.append(('file', (filename, file, 'image/jpeg')))
    
    # Create the multipart-form data payload with all files
    files = files_list

    # Send the request with multipart/form-data
    response = requests.post(url, files=files)

    # Check for errors and log the result
    if response.status_code == 200:
        logging.info("Files are sent successfully")
    else:
        logging.error(f"Error sending files: {response.status_code}")

def main():
    # Example usage:
    directory_path = '/path/to/your/images'
    upload_url = 'http://your-server/upload'
    send_images(directory_path, upload_url)

if __name__ == "__main__":
    main()