import argparse
from filters import Amaterasu as ammy

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='main.py', usage='%(prog)s', description='', epilog='')

    parser._positionals.title = 'Positional arguments'
    parser._optionals.title = 'Optional arguments'

    # might need subparser
    # logic -> 
    #   if inplace is selected, output_dir will be input_dir 
    #   if inplace not selected then output_dir needs to be given
    #   could use terminal gui and make a menu like vuejs [**]
    parser.add_argument('--inplace', type=str2bool, nargs='?', const=True, default=False, help="Overwrite existing video file.")
    parser.add_argument('-o','--output_dir', type=str, required=True, help="Directory to save video file.")

    blur_parsers = parser.add_subparsers(help='sub-command help')

    #hopefully this works as intended, will run once i have more filters :)
    parser_blur = blur_parsers.add_parser('-b','--blur', choices=['faces','license'], help='Object in video you want to blur')
    parser_blur.add_argument('-t','--type', choices=['pixel','gaussian'], help='type of blur to be added')
