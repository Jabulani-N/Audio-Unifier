#!/usr/bin/env python3
"""
contains modules for
    acquiring metadata
    assigning metadata
of an audio file

different formats have different modules
"""

import mutagen

def retrieve_metadata_mp3(source_address):
    source_audio=mutagen.File(source_address)

    # go through all present metadata
    for key, value in source_audio.items():
        # debug print
        print("time to find some metadata!")
        print(f"{key}: {value}")


if __name__ == '__main__':
    # test mode
    print("you are running a test for metadata_manipulator!\
\nyou'll be prompted to enter a mp3 file to list metadata\
\n\nGood luck!")
    source_audio = input("what file do you wanna investigate?")
    retrieve_metadata_mp3(source_audio)
