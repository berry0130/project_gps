import random
import string
import cherrypy
from bs4 import BeautifulSoup



class gps(object):

    def __init__(self):
        self.lat = 23
        self.longti= 121

    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
            <body>
                <form method="get" action="generate">
                </form>
            </body>
        </html>"""
    @cherrypy.expose
    def generate(self, latitude , longtitude):
        # soup = BeautifulSoup(open("iframetest.html"), "html.parser")
        # pid = soup.find('script')
        # long=pid.get_text().encode('utf-8')
        # for i in range(6):
        #     de_log=longtitude.encode('utf-8')
        #     long=long[:88+i] + de_log[i] + long[88+i+1:]
        # f = open("iframetest.html", "r")
        # return f
        self.lat= latitude
        self.longti = longtitude
        lat = self.lat.encode('utf-8')
        longti = self.longti.encode('utf-8')
        print((type)(lat))
        html_str = """
        <!DOCTYPE html>
        <html>
        <head> 
        </head>

        <body>
                    <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d28924.473319386892!2d"""+longti+"""!3d"""+lat+"""!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2stw!4v1585296231311!5m2!1sen!2stw" width="600" height="450" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
                    <style>.mapouter{position:relative;text-align:right;height:500px;width:600px;}.gmap_canvas {overflow:hidden;background:none!important;height:500px;width:600px;}</style>
        </body>
        </html>
        
        """
        Html_file = open("gps_show.html", "w") 
        Html_file.write(html_str)
        Html_file.close()
        f = open("gps_show.html", "r")
        return f

 

if __name__ == '__main__':
    print(type("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14459.749335580087!2d121.5599039!3d25.0362007!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3442aba3dd463e5d%3A0x4842fad8acd9a1d2!2sYongchun%20Station!5e0!3m2!1sen!2stw!4v1584673199805!5m2!1sen!2stw" ))
    cherrypy.quickstart(gps())
