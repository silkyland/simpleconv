# Audio Conversion Script

A simple script to convert audio files from .m4a to .mp3 or .wav format.

### Requirements

Python
ffmpeg or avconv

### Installation

```bash
pip install -r requirements.txt
```

### Change Permission

```bash
chmod +x conv-cli.command
```

### Usage

```bash
./conv-cli.command -i [input_file.m4a] -o [output_format (mp3 or wav)] -n [new_file_name]
```

Example:

```bash
./conv-cli.command -i a.m4a -o mp3 -n "newname"
```

### Note

If ffmpeg or avconv is not found on your system, the script will prompt you to install it.

### Limitations

The script only supports converting .m4a files to either .mp3 or .wav format. If you try to convert a different file type, you will get an error message.
