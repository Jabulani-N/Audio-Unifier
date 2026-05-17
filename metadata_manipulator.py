#!/usr/bin/env python3
"""
contains modules for
    acquiring metadata
    assigning metadata
of an audio file

different formats have different modules
"""

import mutagen
from mutagen.mp4 import MP4
from mutagen.easyid3 import EasyID3

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

def metadata_mp3_to_m4a(source_mp3_address, recieving_m4a):
    """
    use me when the source was mp3 and the target is m4a / mp4
    note that mutagen only supports m4a as an extensoin of mp4
    """
    # safely get tags from source
    try:
        src_mp3_tags = EasyID3(source_mp3_address)
    except Exception as the_problem:
        print("failed to import tags")
        print("due to exception:", the_problem)
        src_mp3_tags = {}
    target_m4a = MP4(recieving_m4a)
    tag_equivalents = {
        # "mp3 tag" : "M4A tag"
        "title": "\xa9nam",
        "artist": "\xa9ART",
        "album": "\xa9alb",
        "genre": "\xa9gen",
        "lyrics": "\xa9lyr", # this is the tag, but it may not allow direct transfer
        "date": "\xa9day",
        "tracknumber": "trkn",   # mp3 uses text tack/total; MP4 uses tuple (track, total)
        "discnumber": "disk",
        "composer": "\xa9wrt",
        "comment": "\xa9cmt",
        }
    for mp3_tag, m4a_tag in tag_equivalents.items():
        if mp3_tag in src_mp3_tags:
            current_mp3_content = src_mp3_tags.get(mp3_tag)
            # mp3 uses text tack/total
            # MP4 uses tuple (track, total)
            print("assigning tag:", m4a_tag)
            if mp3_tag in ("tracknumber", "disknumber"):
                #text formatting
                try:
                    content_parts = current_mp3_content[0].split("/")
                    target_m4a[m4a_tag] = [(int(content_parts[0]) or 0), (int(content_parts[1] or 0))]
                except Exception:
                    print("failed to assign tag", m4a_tag, "from", mp3_tag)
            else:
                target_m4a[m4a_tag] = current_mp3_content

if __name__ == '__main__':
    # test mode
    print("you are running a test for metadata_manipulator!\
\nyou'll be prompted to enter a mp3 file to list metadata\
\n\nGood luck!")
    source_audio = input("what file do you wanna investigate?")
    print(retrieve_metadata(source_audio))
