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

## Preliminary research

 - [x] find a library that converts an audio file
 * `pydub` from https://pydub.com
   * this seems to need ffmpeg installed to the current env, so it won't be portable if I use it. I'll use the same lib I used in video conversion.

## notes to self

for some reason creating the linux python venv was annoying, so i'm linking how I did it for future troubleshooting: https://python.land/virtual-environments/virtualenv#Python_venv_activation

* reminder you use `python -m pip install modulename`

## Tasks

### 01

- [ ] copy format from `named vid 2 m4a` from `vid2aud` repo to make it take a given SINGLE FILE input and convert it to a PROVIDED FILETYPE
  - [ ] script that takes any filetype and converts it to one
    - [ ] mp3
    - [x] m4a
    - [ ] wav
      - fluff. it's really worthless to convert *into* a `.wav` file, but we can have it for completion's sake.
      - "`pcm_s16le` for 16-bit wav and `pcm_s32le` for 32-bit wav."
    - [ ] ogg
      - vorbis audio codec. [moviepy uses `libvorbis`](https://zulko.github.io/moviepy/reference/reference/moviepy.video.VideoClip.VideoClip.html)

### 02

  - [ ] script that takes the "endswith" and uses it to identify which converter script to send it to
        - we have one in vid2aud

### 03

 - [ ] script that recieves a text variable `chosen_output_format` and uses it to append relevant extension (mp3, m4a, etc) to the end of a filename, after removing the extension

### 04

 - [ ] script that strips extension from a given filename and returns filename without extension
   - vid2aud repo should have a script for this within one of the modules, because we use that funcitonality for creating the audio name
   - this will be used alongside the above scrip that returns the extensionless filename to create the desired final filename

### 05

 - [ ] script that creates final desired filename using extension stripper and extension adder to remove previous file extension and replace it with desired final file etension
   - check vid2aud repo to see if we have this funciontality already


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

  - [ ] make it possible to choose `preset` for encoder speed.
    - moviepy default is medium.
    - I'd like to usually use `veryslow`, but other users may not