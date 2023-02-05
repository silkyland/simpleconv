import argparse
import pydub

parser = argparse.ArgumentParser(description='Convert an .m4a file to either an .mp3 or a .wav file.')
parser.add_argument('-i', '--input', type=str, help='Input file name')
parser.add_argument('-o', '--output', type=str, help='Output format (mp3 or wav)')
parser.add_argument('--name', type=str, help='New file name')

args = parser.parse_args()

input_file = args.input
output_format = args.output
new_file_name = args.name

if output_format not in ['mp3', 'wav']:
    print('Error: Invalid output format. Please specify either mp3 or wav.')
    exit()

if not input_file.endswith('.m4a'):
    print('Error: Input file is not an .m4a file.')
    exit()

if not new_file_name.endswith('.' + output_format):
    new_file_name += '.' + output_format

audio = pydub.AudioSegment.from_file(input_file, format='m4a')
audio.export(new_file_name, format=output_format)

print(f'{input_file} has been converted to {new_file_name} in {output_format} format.')
