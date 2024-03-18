#!/usr/bin/env python
import os
import requests

def send_images_to_server(source_dir, server_url):
    # Get a list of all files in the source directory
    image_files = [file for file in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, file))]

    # Iterate over the image files and send each one to the server
    for image_file in image_files:
        # Construct the full path to the image file
        image_path = os.path.join(source_dir, image_file)

        # Open the image file in binary mode
        with open(image_path, 'rb') as file:
            # Create a dictionary containing the file field name and file object
            files = {'file': file}

            # Send a POST request with multipart/form-data containing the image file
            response = requests.post(server_url, files=files)

            # Check if the request was successful
            if response.status_code == 200:
                print(f"Image {image_file} was sent successfully.")
            else:
                print(f"Failed to send image {image_file}. Status code: {response.status_code}")

# Example usage:
source_dir = '/home/yael-vm2/task_azure_output'  # Path to the directory containing the images
server_url = 'http://172.212.97.195/upload'  # URL of the HTTP server endpoint
send_images_to_server(source_dir, server_url)