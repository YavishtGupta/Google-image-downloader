from google_images_search import GoogleImagesSearch 
import time

starttime=time.time()

apicred=input("enter your google search api key")
cx=input("enter your google search engine id")
apicred= 'AIzaSyBPFr33Yj7fc7x7Xu1SefIC6uXVht7FClI'
cx= '56f055e935640402c'
# creating object
gis = GoogleImagesSearch(apicred,cx, validate_images=True)



def downloadimages(query):
	arguments = {"q": query,
				"filetype": "png",
				"num":10,}
	try:
		gis.search(search_params=arguments, path_to_dir=f'./{query}/', 
           custom_image_name=query)
	# Handling File NotFound Error 
	except FileNotFoundError: 
		print("No file found")

query = input("Enter the search query: ")

downloadimages(query)

endtime=time.time()
print(f"Time taken for downloading images: {endtime-starttime:.2f} seconds")