#!/usr/bin/env python3
"""
summons selection box scripts to determine settings,
then runs input_to_output to convert relevant files
"""


format_picker = __import__('pick_desired_format').pick_format
folder_picker = __import__('pick_dir').select_stage
pick_one_of_two = __import__('pick_one_of_two').ask_two_options
converter_ffmpeg = __import__('input_to_output').extract_from_dir


folder_input = folder_picker("Which folder do you want to format files from?")
folder_output = folder_picker("Where do you want to place converted files?")
#user selects target format
target_format = format_picker()
include_vids = pick_one_of_two("Yes", "No",
                               "Include Video files?",
                               "Do you want to convert videos as well?")
# run converter based on selections made
converter_ffmpeg(input_dir=folder_input + "/", output_dir=folder_output + "/",
                     target_format=target_format, include_vids=include_vids)
