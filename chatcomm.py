from request import request
import requests
# This is an API that allows the user to send information to a server to be stored in a database, and receive an id representing the number of the
# informaiton in the database
# This is a standalone API that has no compatibility 
# Retrieve the latest posts since their last post
# Retrieve the last n number of posts

class chatroom:
    def __init__(self, url):
        self.url = url
    def post(self, text):
        newurl = self.url + 'lastn/'
        newurl2 = self.url + 'posts'
        request.post(text, newurl2)
        r = request.lastn(1, newurl)

        return r[0]['id']
    def getSince(self, id):
        newurl = self.url + 'getsince/'
        r = request.getSince(id, newurl)
    
        return r


