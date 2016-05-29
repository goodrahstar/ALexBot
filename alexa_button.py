# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 11:34:30 2016

@author: rahul_z_kuma
"""

import web
import speak as alexa


urls = ('/alexa', 'Alexa')

class Alexa:
    def GET(self):
        print alexa.button()
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head></head><body>                
                <form method="POST" enctype="multipart/form-data" action="">
                <br>
                <br/><br>
                <input type="submit" />
                </form>
                </body></html>"""

    def POST(self):
        try:
            print alexa.button()
            raise web.seeother('/alexa')
                
        except Exception():
            print Exception.message()

 

if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()