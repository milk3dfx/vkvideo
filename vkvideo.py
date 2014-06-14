from urllib2 import Request, urlopen, URLError
import urllib
from time import gmtime, strftime, sleep

class vkVideo:
	def __init__(self, url):
		self.direct_urls = {}
		self.url = url
		req = Request(self.url)
		response = urlopen(req)

		page_data = response.read()
		for res in [240,360,480,720]:
			direct_url = self.findURL(page_data,res)
			if direct_url != None:	
				self.direct_urls[res] = direct_url
			
	def findURL(self, page_str, res):
		try:
			att = "url"+str(res)
			start_ind = page_str.index(att)
			end_ind = page_str.index("?",start_ind)
			url = page_str[(start_ind+len(att)+1):end_ind]
			if "video_ext.php" not in url:
				url = url[4:]
				url = url.replace("\\\\\/", "/")
			return url
		except:
			return None

	def getDirectUrl(self, res):
		if res in self.direct_urls.keys():
			return self.direct_urls[res]
		else:
			return None
			
	def getResolutions(self):
		return list(self.direct_urls.keys())
	
	def download(self, name="", res=-1, reporthook = None):
		if res == -1:
			res = max(self.getResolutions())
		if name == "":
			name = strftime("%m-%d-%Y-%H-%M-%S", gmtime())
		response = urllib.urlretrieve(self.getDirectUrl(res), (name + ".mp4"), reporthook)
