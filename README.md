# Mediapy
Mediapy is a script that enables you to download audio or video files from Youtube (singular or playlist).

### Dependencies
- pytube (for getting the content)
- progress (for the download visual)
- selenium (for scarping of links)
- ffmpeg (for performing conversions)

### Usage
Clone this repository.
Go to the root directory of this project.

To get a single video file,
```sh
$ python3 script.py s v [paste your video link]
```
To get a video playlist,
```sh
$ python3 script.py p v [paste your playlist link]
```
To get a single audio file (extract audio from the given video),
```sh
$ python3 script.py s m [paste your video link]
```
To get a video playlist (extract audio from each given video),
```sh
$ python3 script.py p m [paste your playlist link]
```
### Further Development
- add code for error handling
- would love to get suggestions from the open source community
