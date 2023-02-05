#!/usr/bin/env python3
import argparse
import pydub
import tkinter as tk
from tkinter import filedialog
# import os
import os 

def convert_audio():
    input_file = input_entry.get()
    output_format = output_entry.get()
    new_file_name = name_entry.get()

    if output_format not in ['mp3', 'wav']:
        result_label.config(text='Error: Invalid output format. Please specify either mp3 or wav.')
        return

    if not input_file.endswith('.m4a'):
        result_label.config(text='Error: Input file is not an .m4a file.')
        return

    if not new_file_name:
        new_file_name = os.path.splitext(input_file)[0] + '.' + output_format

    if not new_file_name.endswith('.' + output_format):
        new_file_name += '.' + output_format
        new_file_name = os.path.join(os.path.dirname(input_file), new_file_name)


    audio = pydub.AudioSegment.from_file(input_file, format='m4a')
    audio.export(new_file_name, format=output_format)

    # result_label.config(text=f'{input_file} has been converted to {new_file_name} in {output_format} format.')

    # alert dialog
    alert = tk.Toplevel()
    alert.title("Alert")
    alert.geometry("300x100")
    alert_label = tk.Label(alert, text=f'{input_file} has been converted to {new_file_name} in {output_format} format.')
    alert_label.pack(pady=(10,0))
    alert_button = tk.Button(alert, text="OK", command=alert.destroy)
    alert_button.pack(pady=(10,0))



def browse_file():
    file_path = filedialog.askopenfilename()
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

root = tk.Tk()
root.title("Audio Converter")

input_label = tk.Label(root, text="Input File:")
input_label.grid(row=0, column=0, pady=(10,0))

input_entry = tk.Entry(root)
input_entry.grid(row=0, column=1, pady=(10,0))

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=0, column=2, pady=(10,0))

output_entry = tk.StringVar(root)
output_entry.set("mp3") # default value

output_label = tk.Label(root, text="Output Format:")
output_label.grid(row=1, column=0, pady=(10,0))

output_format_mp3 = tk.Radiobutton(root, text="mp3", variable=output_entry, value="mp3")
output_format_mp3.grid(row=1, column=1, padx=(10,0), pady=(10,0), sticky="w")

output_format_wav = tk.Radiobutton(root, text="wav", variable=output_entry, value="wav")
output_format_wav.grid(row=1, column=1, padx=(80,0), pady=(10,0), sticky="w")

name_label = tk.Label(root, text="New File Name:")
name_label.grid(row=2, column=0, pady=(10,0))

name_entry = tk.Entry(root)
name_entry.grid(row=2, column=1, pady=(10,0))

convert_button = tk.Button(root, text="Convert", command=convert_audio)
convert_button.grid(row=3, column=1, pady=(10,0))

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=1, pady=(10,0))

root.mainloop()
