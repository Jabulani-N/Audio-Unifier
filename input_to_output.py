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

list_subdirs = __import__('list_folders_in_folder').list_dirs
list_files = __import__('list_files_in_folder').list_files
# we don't yet know which converter we'll use, so we import all
converter_to_mp3 = __import__('ffmpeg_to_libmp3lame_codec').named_aud_to_libmp3lame
converter_to_m4a = __import__('ffmpeg_to_aac_codec').named_aud_to_aac
converter_to_wav = __import__('ffmpeg_to_pcm_s16le_codec').named_aud_to_pcm16
converter_to_ogg = __import__('ffmpeg_to_libvorbis_codec').named_aud_to_libvorbis


def extract_from_dir(input_dir="./input/", output_dir="./output/",
                     target_format=".m4a", include_vids=False):
    """
    give it a dir, and it'll loop through each input file within
    and put it in the designated or default output dir
    you could even put them in the source dir if you want
    """
    types_of_input_file = [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".raw", ".m4a", ".opus"]
    vid_formats = [".mp4", ".mov"]
    if include_vids:
        for vid_format in vid_formats:
            types_of_input_file.append(vid_format)
    # makes it not include files that are already correct format
    types_of_input_file = [item for item in types_of_input_file if item != target_format]
    target_vid_titles = np.array([])
    failed_files = []
    subdirs = list_subdirs(input_dir)

    # if there are subdirs, do them first
    if subdirs:
        for subdir in subdirs:
            input_subdir = input_dir + subdir + "/"
            output_subdir = output_dir + subdir + "/"
            extract_from_dir(input_subdir, output_subdir)

    for input_type in types_of_input_file:
        print("About to add files of extension:", input_type)
        target_vid_titles = np.append(target_vid_titles,(list_files(input_dir, input_type)))
        print("Just added files of extension:", input_type)

    target_vid_titles = target_vid_titles.flatten()
    print("All file types collected.\nTotal list of files to be converted:", target_vid_titles)

    # choose which converter to use based on target format
    if target_format.casefold() == ".mp3".casefold():
        converter = converter_to_mp3
    elif target_format.casefold() == ".m4a".casefold():
        converter = converter_to_m4a
    elif target_format.casefold() == ".wav".casefold():
        converter = converter_to_wav
    elif target_format.casefold() == ".ogg".casefold():
        converter = converter_to_ogg
    else:
        raise ValueError("Invalid output target format selected.")

    # run the chosen converter on every target file
    # variables are named with "vid" because of reusing code.
    for vid_name_full in target_vid_titles:
        vid_name_stem = Path(vid_name_full).stem
        output_aud_file_name = vid_name_stem + target_format
        if Path(output_dir + output_aud_file_name).exists():
            print(output_dir + output_aud_file_name," already exists, so it is skipped")
        else:
            print("sending '", vid_name_full, "' in '", input_dir, "' to", converter)
            print("to ask", converter, "to make '", output_aud_file_name, "' in", output_dir)
            print("type of file name full is", type(vid_name_full))
            failed_files.append(converter(vid_name_full, output_aud_file_name, input_dir, output_dir))

    # if list of failures has no actual failures
    if all(flag == None for (flag) in failed_files):
        print("\n\nAll conversions were successful!\n")
    else:
        print("\n\nThe following files failed to be converted and were skipped:\n")
        for failure in failed_files:
            if failure is not None:
                print(failure)
        print("")

if __name__ == '__main__':
    """runs the converter for audio to m4a conversion"""
    extract_from_dir()
