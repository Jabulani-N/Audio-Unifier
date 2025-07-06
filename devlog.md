# Devlog

Planning space and tasklist.


**Contents**

- [Devlog](#devlog)
  - [Preliminary research](#preliminary-research)
  - [notes to self](#notes-to-self)
  - [Tasks](#tasks)
    - [01](#01)
    - [02](#02)
    - [03](#03)
    - [04](#04)
    - [05](#05)
    - [06](#06)
    - [07](#07)
    - [08](#08)
    - [09](#09)
    - [Extra](#extra)
  - [Bugs](#bugs)
    - [Current](#current)

## Preliminary research

 - [x] find a library that converts an audio file
 * `pydub` from https://pydub.com
   * this seems to need ffmpeg installed to the current env, so it won't be portable if I use it. I'll use the same lib I used in video conversion.

## notes to self

for some reason creating the linux python venv was annoying, so i'm linking how I did it for future troubleshooting: https://python.land/virtual-environments/virtualenv#Python_venv_activation

* reminder you use `python -m pip install modulename`

## Tasks

### 01

- [x] copy format from `named vid 2 m4a` from `vid2aud` repo to make it take a given SINGLE FILE input and convert it to a PROVIDED FILETYPE
      - [ ] we have one that works, so copypaste it and change where needed. new file for easier testing
  - [x] script that takes any filetype and converts it to one
    - [x] mp3
      - [x] `libmp3lame` codec
    - [x] m4a
      - [x] `aac` codec
    - [x] wav
      - fluff. it's really worthless to convert *into* a `.wav` file, but we can have it for completion's sake.
      - "`pcm_s16le` codec for 16-bit wav and `****pcm_s32**le**` for 32-bit wav."
    - [x] ogg
      - vorbis audio codec. [moviepy uses `libvorbis`](https://zulko.github.io/moviepy/reference/reference/moviepy.video.VideoClip.VideoClip.html)

### 02

  - [x] copy and update `input_to_output.py`
    - [x] update will:
      - [x] add a slot to recieve `target_format`
      - [x] update `types_of_input_file` to be a list of ffmpeg-enabled extensions (make it default to all of them), and then say `types_of_input_file = types_of_input_file[where except indices containing  target_format]`
        - `types_of_input_file = [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".raw", ".m4a", ".opus"]`
          - if the user wants to additionally extract audio from video files, append `[".mov", ".mp4"]` to `types_of_input_file` and flatten
      - [x] duplicate `converter` to one to import each `ffmpeg_to_[format]` script
        -  for example, there will be a `converter_mp3` that = `ffmpeg_to_libmp3lame_codex`, and a `converter_m4a` that = `ffmpeg_to_aac_codec`
     -  [x] skip files that are already in requested format

### 03

 - [x] script that recieves a text variable `chosen_output_format` and uses it to append relevant extension (mp3, m4a, etc) to the end of a filename, after removing the extension

### 04

 - [x] script that strips extension from a given filename and returns filename without extension
   - vid2aud repo should have a script for this within one of the modules, because we use that funcitonality for creating the audio name
   - this will be used alongside the above scrip that returns the extensionless filename to create the desired final filename

### 05

 - [x] script that creates final desired filename using extension stripper and extension adder to remove previous file extension and replace it with desired final file etension
   - check vid2aud repo to see if we have this funciontality already
   - it's part of input_to_output


### 06

 - [ ] ui window to choose folder
   - vid2aud has this

### 07

 - [ ] ui window to choose new file format

### 08

 - [ ] main script to summon the relevant scripts
   - vid2aud has usable format

### 09

- [ ] copy format from vid2aud gui to map out remaining steps

### Extra

  - [x] ~~make it possible to choose [`preset`](https://zulko.github.io/moviepy/reference/reference/moviepy.video.io.ffmpeg_writer.FFMPEG_VideoWriter.html) for encoder speed.~~
    - ~~moviepy default is medium.~~
    - ~~I'd like to usually use `veryslow`, but other users may not~~
    - only applies to videofileclips. cannot be used in [wriitng audio files](https://zulko.github.io/moviepy/reference/reference/moviepy.audio.AudioClip.AudioClip.html#moviepy.audio.AudioClip.AudioClip.write_audiofile).
  - [ ] One can select a `bitrate`, for the audio equivalent within `write_audiofile(filename, fps=None, nbytes=2, buffersize=2000, codec=None, bitrate=None, ffmpeg_params=None, write_logfile=False, logger='bar')` (you can paste that into a search to jump to the entry on writing audio files.)
    - optional

- - - - -

## Bugs

### Current

certain .mp3 files with metadata break moviepy's audiofileclip importer.
* in the course of trying to deal with htis, I updated moviepy from `moviepy-2.1.2` to `moviepy-2.2.1`.
