import os
import requests

def send_files_to_server(url, files):
    try:
        response = requests.post(url, files=files)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Files are sent successfully")
    except requests.exceptions.RequestException as e:
        print("Error sending files:", e)

def main():
    # URL of the server endpoint to which the files will be sent
    server_url = "http://172.212.97.195/upload"

    # Directory containing the images
    images_directory = "/home/yael-vm2/task_azure_output"

    # Initialize an empty dictionary to store files
    files_to_send = {}

    # Iterate over files in the directory
    for filename in os.listdir(images_directory):
        file_path = os.path.join(images_directory, filename)
        if os.path.isfile(file_path):
            # Open the file and read its contents
            with open(file_path, "rb") as file:
                # Add the file to the dictionary with its original filename
                files_to_send[filename] = file.read()

    # Send the files to the server
    send_files_to_server(server_url, files_to_send)

if __name__ == "__main__":
    main()
