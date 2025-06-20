#!/usr/bin/env python3
"""
This module is a modified version of input_to_output.py from Vid2Aud.

this module puts together previously created scripts
to automatically take exposed ffmpeg audio files in inputs dir
and convert them to selected format in output dir

Uses recursion to make handle layered dirs.

DON'T DO THE BELOW IN THIS SCRIPT
user inputs to add for execution selection - these go in GUI
[ ] what output format do you want?
[ ] do you want to create copies of any file already using that extension?
[ ] do you want to convert video files to audio?
"""

import numpy as np
from pathlib import Path

list_files = __import__('list_files_in_folder').list_files
# converter = __import__('named_vid_to_m4a').named_vid_to_m4a
converter_to_mp3 = __import__('ffmpeg_to_libmp3lame_codec.py').
list_subdirs = __import__('list_folders_in_folder').list_dirs


def extract_from_dir(input_dir="./input/", output_dir="./output/",
                     target_format=".m4a", include_vids=False):
    """
    give it a dir, and it'll loop through each vid file within
    and put it in the designated or default output dir
    you could even put them in the source dir if you want
    """
    types_of_input_file = [".mp4"]
    target_vid_titles = np.array([])
    subdirs = list_subdirs(input_dir)

    # if there are subdirs, do them first
    if subdirs:
        for subdir in subdirs:
            input_subdir = input_dir + subdir + "/"
            output_subdir = output_dir + subdir + "/"
            extract_from_dir(input_subdir, output_subdir)

    for input_type in types_of_input_file:
        print("about to add files of extension", input_type)
        target_vid_titles = np.append(target_vid_titles,(list_files(input_dir, input_type)))
        print("just added files of extension", input_type)

    target_vid_titles = target_vid_titles.flatten()
    print("All file types collected.\nTotal list of files to be converted:", target_vid_titles)

    # have imported all converters
    # choose which converter to use based on target format
    if target_format.casefold() == "m4a".casefold():
        converter = 
    # run the chosen converter on every target file
    for vid_name_full in target_vid_titles:
        vid_name_stem = Path(vid_name_full).stem
        output_aud_file_name = vid_name_stem + ".m4a"
        print("sending '", vid_name_full, "' in '", input_dir, "' to converter")
        print("to ask converter to make '", output_aud_file_name, "' in", output_dir)
        print("type of vid name full is", type(vid_name_full))
        converter(vid_name_full, output_aud_file_name, input_dir, output_dir)

if __name__ == '__main__':
    """runs the converter for vid to m4a conversion"""
    extract_from_dir()
