# chopchop

Chopchop is a tool that automatically edits videos for you. Chopchop can create jumpcuts for video files, i.e.remove silence, and make you sound really witty! 

As a next step I hope to implement automatic music video creation, where a user simply inputs an audio file and a directory containing a bunch of videos to be cut together.

## Installation
Chopchop relies heavily on [ffmpeg](http://ffmpeg.org), and this needs to be installed on your machine in order for chopchop to work. 

And then of course we need to install a million dependencies. Nah, kidding. Chopchop uses only the Python standard library. Nothing else needs to be installed! 

## Running
```bash
python main.py --file yourvideofile.mp4
```
