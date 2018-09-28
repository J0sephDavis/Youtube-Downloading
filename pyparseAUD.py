from pytube import YouTube
import time
import datetime
from pytube import YouTube
import os

def downloadYouTube(videourl, path, cnt):
	try:
		yt = YouTube(videourl)
		yt2 = yt.streams.filter(only_audio=True).first()
		if not os.path.exists(path):
			os.makedirs(path)
		yt2.download(path)
		print(yt.title)
		print('Downloaded {} | {}'.format(cnt, datetime.datetime.now()))
	except Exception as e:
		print("ERROR: ", e)



filepath = 'thewall.txt'
with open(filepath) as fp:  
	line = fp.readline()
	cnt = 1
	while line:
		line = fp.readline()
		downloadYouTube('{}'.format(line.strip()), './test', cnt)
		cnt += 1