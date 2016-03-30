#coding = utf-8
import time
import comm
from urlparse import *
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

def claw_url(url):
	if(url != ''):
		url_info = urlparse(url)
		driver.get(url)
		print( "Current_url:"+driver.current_url )
		driver.get_screenshot_as_file("/tmp/SitePic/"+url_info.netloc+".png")

def get_input(filename):
	input = open(filename)

	for line in input:
		claw_url( comm.get_302_url(line[:-1]) )

if __name__ == "__main__":
	comm.set_logging()
	
	driver = webdriver.PhantomJS('/home/elfsong/phantomjs-2.1.1/bin/phantomjs')

	get_input("input.txt")
	
	driver.quit()
