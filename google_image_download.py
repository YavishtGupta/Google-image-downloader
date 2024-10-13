import os
from google_images_search import GoogleImagesSearch 
from dotenv import load_dotenv
import time

load_dotenv()

# Retrieve credentials from environment variables
apicred = os.getenv("GOOGLE_SEARCH_API_KEY")
cx = os.getenv("GOOGLE_SEARCH_ENGINE_ID")

starttime = time.time()

# Ensure the credentials are set
if not apicred or not cx:
    print("API credentials are not set in environment variables\n")
    apicred=input("Please enter your API key:")
    print("\n")
    cx=input("Please enter your search engine ID:")

# Creating object
gis = GoogleImagesSearch(apicred, cx, validate_images=True)

def downloadimages(query,num_images):
    arguments = {
        "q": query,
        "filetype": "png",
        "num": num_images,
    }
    try:
        gis.search(search_params=arguments, path_to_dir=f'./results/{query}/', custom_image_name=query)
    except FileNotFoundError: 
        print("No file found")

query = input("Enter the search query: ")
num_images = int(input("Enter the number of images to download: "))

downloadimages(query,num_images)

endtime = time.time()
print(f"Time taken for downloading images: {endtime - starttime:.2f} seconds")
