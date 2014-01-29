# use curl to get webpage source code

'''
Usage:

    mypage = GetPage("http://udn.com/NEWS/BREAKINGNEWS/")
    
    ===  create a object ===

    testcurl = pycurl.Curl()
    testcurl.setopt(testcurl.URL, mypage.url)
    testcurl.setopt(testcurl.WRITEFUNCTION, mypage.read_page)
    testcurl.perform()
    testcurl.close()

    ===  curl setting ===

    source_code = mypage.return_data


'''

import pycurl

class GetPage:
    def __init__ (self, url):
        self.contents = ''
        self.url = url

    def read_page (self, buf):
        self.contents = self.contents + buf

    def show_page (self):
        print self.contents
    def return_data (self):
    	return self.contents