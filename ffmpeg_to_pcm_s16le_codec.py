#!/usr/bin/env python3
"""
Largely reuses code from ffmpeg to libvorbis


converts one named audio or video video file into
    any audio format that uses pcm_s16le encoding,
given:

    source medium name
    source location directory
    desired output name
    output destination directory

file names required.
default directories exist, but should be specified when used.
"""

import moviepy
from moviepy import AudioFileClip
import os
import sys


def named_aud_to_aac(input_vid_name, output_aud_name,
                     source_loc='./input/',
                     save_loc='./output/'):
    """
    take an input aud name
    take output aud name

    have moviepy turn the audiofileclip into an pcm_s16le format
    """

    print("converter args recieved:")
    print("input aud name:", input_vid_name)
    print("source loc:", source_loc)
    print("output aud name:", output_aud_name)
    print("save loc:", save_loc)
    in_aud_file = source_loc + input_vid_name
    out_aud_file = save_loc + output_aud_name
    # pcm_s16le is used in 16-bit wav files
    # a different codec, pcm_s32le is used in 32-bit wav files
    output_codec = "pcm_s16le"

    print("varibles declared:")
    print("source file is", in_aud_file, "from", source_loc)
    print("create", out_aud_file, "in", save_loc)

    # import audio as AudioFileClip
    orig_audio = AudioFileClip(in_aud_file)
    print("audio file imported as AudioFileClip without incident")

    # audio writing

    # create necessary directories
    os.makedirs(os.path.dirname(out_aud_file), exist_ok=True)
    # save audio as new file
    orig_audio.write_audiofile(out_aud_file, codec=output_codec)
    print("audio file written")
    # close the created clips
    orig_audio.close()
    print("AudioFileClip file closed")


if __name__ == '__main__':
    # test mode
    # running as main prompts user for vid name
    print("you are running a test for the named\
audio to audio file conversion system!\
\n\nThis one tests conversion of ffmpeg-compatible files into 16-bit WAV\
\n\nYou'll be prompted to enter the name\
of the input file, extension included, \
and then what you want the output file to be named.\
\n\nThis is purely funtionality for debugging.\
\nNormally, you won't actually be able to see\
this method work, as it'll be getting called internally\
and automatically.\
\n\nGood luck!\n\n  -- Jabulani Ndhlovu")
    aud_file_to_take = input("What audio file will you convert?: ")
    aud_file_to_give = input("What will you name the converted file?: ")
    print("you want to take",aud_file_to_take,
          "and give audio file", aud_file_to_give)
    named_aud_to_aac(aud_file_to_take,
                     aud_file_to_give)
