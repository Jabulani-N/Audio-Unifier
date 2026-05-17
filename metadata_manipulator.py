#!/usr/bin/env python3
"""
contains modules for
    acquiring metadata
    assigning metadata
of an audio file

different formats have different modules
"""

import mutagen

def retrieve_metadata(source_address):
    """
    returns a list filled with metadata
    """
    source_audio=mutagen.File(source_address)
    meta_list = []
    # go through all present metadata
    for key, value in source_audio.items():
        meta_list.append([key, value])
    return meta_list

def assign_metadata(source_address, meta_list):
    """
    remakes the file source_address
    but containing metadata from meta_list
    """
    return

if __name__ == '__main__':
    # test mode
    print("you are running a test for metadata_manipulator!\
\nyou'll be prompted to enter a mp3 file to list metadata\
\n\nGood luck!")
    source_audio = input("what file do you wanna investigate?")
    print(retrieve_metadata(source_audio))
