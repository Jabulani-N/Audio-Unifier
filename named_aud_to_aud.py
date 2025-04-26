#!/usr/bin/env python3
"""
converts one audio file to
    provided audio format
    default: mp3 audio
given:

    source aud name
    source location directory
    desired output name
    output destination directory

file names required.
default directories exist, but should be specified when used.
"""

from pydub import AudioSegment


def named_aud_to_aud(input_aud_name="Floor of History.wav",
                     output_aud_name="Floor of History.mp3",
                     source_loc='./input/',
                     save_loc='./output/'):

    print("converter args recieved:")
    print("input vid name:", input_aud_name)
    print("source loc:", source_loc)
    print("output aud name:", output_aud_name)
    print("save loc:", save_loc)

    aud_in = source_loc + input_aud_name
    aud_out = save_loc + output_aud_name
