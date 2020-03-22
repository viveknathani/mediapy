#!/usr/bin/env python3
import os
import sys
import pytube
import subprocess
from selenium import webdriver
from progress.bar import FillingSquaresBar

argument_list=sys.argv
SAVE_PATH="download"

identify_content=argument_list[1] # s or p
file_type=argument_list[2] # m or v
url=argument_list[3]

def download_video(link):
    yt=pytube.YouTube(link)
    bar=FillingSquaresBar("Downloading Video : ", suffix="%(percent)d%%")
    for i in range(100):
        stream=yt.streams.first()
        stream.download(SAVE_PATH)
        bar.next()
    bar.finish()

def download_audio(link):
    yt=pytube.YouTube(link)
    bar=FillingSquaresBar("Downloading Audio : ", suffix="%(percent)d%%")
    for i in range(100):
        stream=yt.streams.filter(only_audio=True).first()
        _filename=yt.title.replace(" ", "_")
        _filename=_filename.replace(".", "_")
        _filename=_filename.replace("$", "_")
        _filename=_filename.replace("@", "_")
        _filename=_filename.replace("(", "_")
        _filename=_filename.replace(")", "_")
        mp4_name="download/%s.mp4"%_filename
        mp3_name="download/%s.mp3"%_filename
        stream.download(SAVE_PATH, _filename)
        bar.next()

    print("\nPerforming required conversions...")
    ffmpeg=('ffmpeg -loglevel panic -i %s ' % mp4_name + mp3_name)
    subprocess.call(ffmpeg, shell=True)
    os.remove(mp4_name)
    bar.finish()

if(identify_content=="s" and file_type=="v"):
    download_video(url)

if(identify_content=="s" and file_type=="m"):
    download_audio(url)

if(identify_content=="p"):
    options=webdriver.ChromeOptions()
    options.add_argument('headless')
    browser=webdriver.Chrome(chrome_options=options)
    playlist_link=url

    browser.get(playlist_link)
    my_element=browser.find_element_by_class_name("style-scope ytd-playlist-video-list-renderer")
    a_tag_list=my_element.find_elements_by_xpath("//a[@class='yt-simple-endpoint style-scope ytd-playlist-video-renderer']")

    link_list=[]
    for a_tag in a_tag_list:
        link_list.append(a_tag.get_attribute("href"))

    if(file_type=="v"):
        for i in link_list:
            download_video(i)

    if(file_type=="m"):
        for i in link_list:
            download_audio(i)

print("Task completed.")
