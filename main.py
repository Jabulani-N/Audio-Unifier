#!/usr/bin/env python3
"""
summons selection box scripts to determine settings,
then runs input_to_output to convert relevant files
"""


format_picker = __import__('pick_desired_format').pick_format
folder_picker = __import__('pick_dir').select_stage
pick_one_of_two = __import__('pick_one_of_two').ask_two_options
converter_ffmpeg = __import__('input_to_output').extract_from_dir


def run_gui():
    if __name__ == '__main__': print("welcome to Audio Unifier!\n\nYou \
won't need this terminal,\
so please take a look at \
the window \
to choose which folder you want to convert!")
    folder_input = folder_picker("Which folder do you want to format files from?")
    if not folder_input:
        return
    folder_output = folder_picker("Where do you want to place converted files?")
    if not folder_output:
        return
    # user selects target format
    target_format = format_picker()
    opt1, opt2 = "Yes", "No"
    box_title = "Include Video files?"
    box_text = "Do you want to convert videos as well?"
    include_vids = pick_one_of_two(opt1, opt2,
                                   box_title, box_text)
    if include_vids == "Cancel":
        return
    # run converter based on selections made
    opt1, opt2 = "Start!", "Start Over"
    box_title = "Begin?"
    box_text = "Begin converting media in folder " + folder_input +\
    "\ninto " + target_format + " files\nin folder " + folder_output + "?" +\
    "\n\nProcessing video files as well: " + include_vids
    confirmation = pick_one_of_two(opt1, opt2, box_title, box_text)
    if confirmation == opt1:
        converter_ffmpeg(input_dir=folder_input + "/", output_dir=folder_output + "/",
                     target_format=target_format, include_vids=include_vids)
    elif confirmation == opt2:
        run_gui()

if __name__ == '__main__':
    run_gui()
