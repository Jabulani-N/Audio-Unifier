#!/usr/bin/env python3
"""
This approach was tested and found to not work for freezing,
as it requires installed ffmpeg.
moviepy has inbuilt ffmpeg, so we can use it instead

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

    # save song as audiosegment object
    song = AudioSegment.from_wav(source_loc + input_aud_name)
    print("song saved as AudioSegment")
    # convert and save song from audiosegment
    song.export(save_loc + output_aud_name, format="mp3")
    print("song exported from audiosegment")

if __name__ == '__main__':
    # test mode
    print("you are running a test for the named\
proof of concept audio file conversion system!\
\n\we'll take a default file from the input folder, convert it, \
\n and save the converted version into the default output folder  \
\n\nGood luck!\n\n  -- Jabulani Ndhlovu\n\n")
named_aud_to_aud()
