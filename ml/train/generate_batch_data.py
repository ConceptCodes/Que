# find a random photo from google or pexels
# place que_card in a random spot in photo
# possibly distort image to better roboust the dataset
# do this x times 

import os
import random
import argparse
from PIL import Image
from base_card import QueCard
from google_images_download import google_images_download 

output_dir= ""

def place_que_card(que, card):
    # find a random quadrant
    quadrant = random.randint(0,3)
    # place image in that quadrant
    que = Image(que)
    que.paste(card, (100, 50))
    que.save('{}rocket_pillow_paste_pos.jpg'.format(output_dir), quality=95)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='generate_batch_data.py', usage='%(prog)s [type] output_dir *args', description='Generates a dataset of Que cards.', epilog='When in doubt, more data :)')

    parser._positionals.title = 'Positional arguments'
    parser._optionals.title = 'Optional arguments'

    parser.add_argument('-t', '--type', type=str, choices=['poptag','speed','overlay'], required=True, help='type of que card to generate')
    parser.add_argument('-o', '--output-dir', type=str, help="directory to put images")