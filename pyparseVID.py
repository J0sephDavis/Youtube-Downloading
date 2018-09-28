from pytube import YouTube
import time
import datetime
from pytube import YouTube
import os

def downloadYouTube(videourl, path, cnt):
	try:
		yt = YouTube(videourl)
		yt2 = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
		if not os.path.exists(path):
			os.makedirs(path)
		yt2.download(path)
		print(yt.title)
		print('Downloaded {} | {}'.format(cnt, datetime.datetime.now()))
	except Exception as e:
		print("ERROR: ", e)



filepath = 'electronics.txt'
with open(filepath) as fp:  
	line = fp.readline()
	cnt = 1
	while line:
		line = fp.readline()
		downloadYouTube('{}'.format(line.strip()), './films/Electronics', cnt)
		cnt += 1