import argparse

from detecto import core, utils, visualize

dataset = core.Dataset('cards/')
model = core.Model(['poptag', 'speed', 'overlay'])

model.fit(dataset)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='train_que_card.py', usage='%(prog)s [type] output_dir *args', description='Train computer to detect que card', epilog="When in doubt, more gpu's :)")

    parser._positionals.title = 'Positional arguments'
    parser._optionals.title = 'Optional arguments'

    parser.add_argument('-t', '--type', type=str, choices=['poptag','speed','overlay'], required=True, help='type of que card to generate')
    parser.add_argument('-o', '--output-dir', type=str, help="directory to put images")