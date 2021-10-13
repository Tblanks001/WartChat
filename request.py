import requests, json


class request:
	def post(p, n, url):

		# Calls upon the Flask application to place a dictionary containing both content and name into the database
		# The url http://127.0.0.1:5000/posts is used to call the function 'posts' located in the Flask app

		post = {
		'content': p,
		'name': n
		}
		r = requests.post(url, json = post)
		return r


	def getSince(n, url):

		# Calls upon the Flask application to return the posts made since the post id corresponding to n 
		# The url http://127.0.0.1:5000/getsince/'id' is used to call the function 'getSince(id)' located in the Flask app

		r = requests.get(url + str(n))
		
		return r.json()

	def lastn(n, url):

		# Calls upon the Flask application to return the last n posts
		# The url http://127.0.0.1:5000/lastn/'id' is used to call the function 'lastn(id)' located in the Flask app

		r =  requests.get(url + str(n))

		return r.json()




