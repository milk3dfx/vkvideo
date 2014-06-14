from vkvideo import vkVideo
import os, sys, time
import argparse

def downloading(num,p_size,total):
	size = num*p_size
	if size > total:
		size = total
	print "                                        \r",
	print  size, "of", total, "(", round((float(100*size)/total), 1), "% )",

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Download anime series from Anidub')
	parser.add_argument('name', help='Name of anime series')
	parser.add_argument('link', help='Link from Anidub on anime series')
	parser.add_argument('-r', type=int, nargs='?', default=-1,
	choices=[240, 360, 480,720], help='Resolution (default: max)')
	args = parser.parse_args()
	#link = "http://vk.com/video150568755_168542015"
	
	print "Getting video info"
	i = 0
	while True:
		try:
			video = vkVideo(args.link)
			break
		except:
			print "Retry within 3 seconds"
			time.sleep(3)
			i += 1
			if i == 3:
				print "Video can't be downloaded"
				sys.exit()

	resolutions = video.getResolutions()
	print "Resolutions:", resolutions
	print "Direct url:", video.getDirectUrl(max(resolutions))

	print "Downloading video"
	i = 0
	while True:
		try:
			video.download(args.name, args.r, downloading)
			break
		except:
			print "Retry within 3 seconds"
			time.sleep(3)
			i += 1
			if i == 3:
				print "Video can't be downloaded"
				sys.exit()
