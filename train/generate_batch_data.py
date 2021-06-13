# find a random photo from google or pexels
# place que_card in a random spot in photo
# possibly distort image to better roboust the dataset
# do this 100 times for each category


import os
import random
import argparse
from PIL import Image
from base_card import QueCard
from google_images_download import google_images_download 

output_dir= ""

def get_random_photo(num=100):
    # use google image api to get hold of an image object
    response = google_images_download.googleimagesdownload()
    arguments = {
        "keywords": "party, people, living room, house tour",
        "limit": num,
        "print_urls": True
    } 
    paths = response.download(arguments)  
    print(paths)  

def place_que_card(img, card):
    # find a random quadrant
    #quadrant = random.randint(0,3)
    # place image in that quadrant
    return Image(img).paste(card)

def save_img():
    pass
    # place image in folder of que card


parser = argparse.ArgumentParser(prog='generate_batch_data.py', usage='%(prog)s [type] output_dir *args', description='Generates a dataset of Que cards.', epilog='When in doubt, more data :)')

parser._positionals.title = 'Positional arguments'
parser._optionals.title = 'Optional arguments'

parser.add_argument('-t', '--type', type=str, help='type of que card to generate')
parser.add_argument('-o', '--output-dir', type=str, help="directory to put images")