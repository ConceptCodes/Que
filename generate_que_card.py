import os
import argparse 


def que_card(type, duration: int, meta: dict):
    print('type', type)
    print('duration'. duration)
    print('meta', meta)

output_path= os.path.join(os.getcwd(),'que-cards')

parser = argparse.ArgumentParser(prog='generate_que_card.py', usage='%(prog)s [type] *args', description='Generates a Que card.', epilog='Happy filmaking :)')

parser._positionals.title = 'Positional arguments'
parser._optionals.title = 'Optional arguments'

parser.add_argument('-p', '--poptag', type=str, help='name to be displayed in poptag')
parser.add_argument('-s', '--speed', type=float, help='amount of speed change to video')
parser.add_argument('-d', '--duration', type=int, default=5, help='duration of [type] effect')
parser.add_argument('-o', '--overlay', type=int, help='Color to be overlayed', nargs=3)

args = parser.parse_args()

if args.poptag: que_card(type='poptag', duration=args.duration, meta={'name': args.poptag})
elif args.speed: que_card(type='speed', duration=args.duration, meta={'amt': args.speed})
elif args.overlay: que_card(type='overlay', duration=args.duration, meta={'color': args.overlay}) # add audio and potentially background cropping later

