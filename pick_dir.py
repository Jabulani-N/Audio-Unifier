#!/usr/bin/env python3
"""
prompts user to select a folder
returns address of selected folder
"""

import tkinter as tk
from tkinter import filedialog
import sys
import os

def select_stage(dialogue_box_text="Please select a directory"):
    """
    opens window for user to select a folder
    """

    # Create a hidden root window
    root = tk.Tk()
    # assign icon
    # root.iconbitmap('./icon/icon.ico')
    if getattr(sys, 'frozen', False):
        # bundled as executable
        # application_path = './icon/'
        try:
            application_path = sys._MEIPASS
        except AttributeError:
            application_path = os.path.abspath(".")

    else:
        # runninng the raw python code
        application_path ='./icon/'

    # application_path ='./icon/'
    # print("application path is: \n", application_path)
    icon_path = os.path.join(application_path, 'icon.ico')
    root.iconbitmap(icon_path)
    # Hide the root window
    root.withdraw()

    # Prompt the user to select a folder
    dirloc = filedialog.askdirectory(title=dialogue_box_text)

    print(f"Selected folder: {dirloc}")
    return dirloc

if __name__ == '__main__':
    select_stage()
