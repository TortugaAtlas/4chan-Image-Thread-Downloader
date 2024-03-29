import os
import sys
import requests
import tkinter as tk
from tkinter import ttk, messagebox
from fetch_images_4chan import fetch_images_from_4chan

class FourChanImageDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("4chan Image Downloader")
        self.root.geometry("400x200")

        # Create a style for the labels
        self.label_style = ttk.Style()
        self.label_style.configure("TLabel", foreground="#333", font=("Helvetica", 12))

        # Create a style for the buttons
        self.button_style = ttk.Style()
        self.button_style.configure("TButton", foreground="white", background="#007bff", font=("Helvetica", 12))

        # Create a style for the entry fields
        self.entry_style = ttk.Style()
        self.entry_style.configure("TEntry", foreground="#333", font=("Helvetica", 12))

        # Create and place the widgets
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for better layout
        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Board label and entry
        self.board_label = ttk.Label(self.frame, text="Board:")
        self.board_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.board_entry = ttk.Entry(self.frame, width=30)
        self.board_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Thread ID label and entry
        self.thread_label = ttk.Label(self.frame, text="Thread ID:")
        self.thread_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.thread_entry = ttk.Entry(self.frame, width=30)
        self.thread_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Folder label and entry
        self.folder_label = ttk.Label(self.frame, text="Folder:")
        self.folder_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.folder_entry = ttk.Entry(self.frame, width=30)
        self.folder_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Download button
        self.download_button = ttk.Button(self.frame, text="Download Images", command=self.download_images, style="TButton")
        self.download_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    def create_folder(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def download_image(self, url, folder):
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(folder, os.path.basename(url)), 'wb') as f:
                f.write(response.content)
                print(f"Downloaded: {url}")
        else:
            print(f"Failed to download: {url}")

    def fetch_images_from_4chan(self):
        board = self.board_entry.get()
        thread_id = self.thread_entry.get()
        folder = self.folder_entry.get()

        if not all([board, thread_id, folder]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            fetch_images_from_4chan(board, thread_id, folder)
            messagebox.showinfo("Success", "Images downloaded successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download images: {str(e)}")

    def download_images(self):
        self.fetch_images_from_4chan()

def main():
    root = tk.Tk()
    app = FourChanImageDownloaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
