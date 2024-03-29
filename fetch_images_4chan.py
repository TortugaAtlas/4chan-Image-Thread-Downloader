import os
import sys
import requests

# Function to create a folder if it doesn't exist
def create_folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to download an image and save it to a folder
def download_image(url, folder):
    create_folder(folder)  # Create folder if it doesn't exist
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(folder, os.path.basename(url)), 'wb') as f:
            f.write(response.content)
            print(f"Downloaded: {url}")
    else:
        print(f"Failed to download: {url}")

# Function to fetch images from 4chan thread and save them in a folder
def fetch_images_from_4chan(board, thread_id, folder):
    url = f"https://a.4cdn.org/{board}/thread/{thread_id}.json"
    response = requests.get(url)
    if response.status_code == 200:
        thread_data = response.json()
        posts = thread_data["posts"]
        for post in posts:
            if "tim" in post and "ext" in post:
                image_url = f"https://i.4cdn.org/{board}/{post['tim']}{post['ext']}"
                download_image(image_url, folder)
    else:
        print(f"Failed to fetch thread data from 4chan: {url}")

# Main function
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./fetch_images.py <board> <thread_id> <folder>")
        sys.exit(1)

    board = sys.argv[1]
    thread_id = sys.argv[2]
    folder = sys.argv[3]

    fetch_images_from_4chan(board, thread_id, folder)
