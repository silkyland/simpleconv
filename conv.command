#!/bin/bash

command -v ffmpeg >/dev/null 2>&1 || command -v avconv >/dev/null 2>&1 || { echo >&2 "Error: ffmpeg or avconv is required but not found. Please install it and try again."; exit 1; }

input_file=""
output_format="wav"
new_file_name=""

while getopts "i:o:n:" opt; do
  case $opt in
    i)
      input_file="$OPTARG"
      ;;
    o)
      output_format="$OPTARG"
      ;;
    n)
      new_file_name="$OPTARG"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

if [ -z "$input_file" ]; then
  echo "Error: Input file is required."
  exit 1
fi

if [ -z "$new_file_name" ]; then
  new_file_name="${input_file%.*}.$output_format"
fi

if [ "$output_format" != "mp3" ] && [ "$output_format" != "wav" ]; then
  echo "Error: Invalid output format. Please specify either mp3 or wav."
  exit 1
fi

if [ "$input_file" != *.m4a ]; then
  echo "Error: Input file is not an .m4a file."
  exit 1
fi

python3 conv-cli.py --input "$input_file" -o "$output_format" --name "$new_file_name"
