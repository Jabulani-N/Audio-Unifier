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
