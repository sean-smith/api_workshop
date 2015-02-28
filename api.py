
from flask import Flask, jsonify, request
import time, requests, random,json
import xml.dom.minidom as parse
app = Flask(__name__)

def reddit_request(url):
	hdr = {'User-Agent' : 'btc/1.0 by btc_sentiment'}
	r = requests.get(url, headers=hdr)
	return r.json()

def imgur_url(url):
	r = requests.get(url)
	d = parse.parseString(r.text)
	print(d.documentElement.nodeName)

@app.route("/")
def hello():
	data = {
	"Version": 1.0,
	"Name": "Sean's API"
	}
	return jsonify(**data)

@app.route("/time")
def tm():
	t = time.localtime()
	year = t.tm_year
	month = t.tm_mon
	day = t.tm_mday
	hour = t.tm_hour
	seconds = t.tm_sec
	minute = t.tm_min
	data = {
	"year": year,
	"day": day,
	"month": month,
	"hour": hour,
	"seconds": seconds,
	"minute": minute
	}
	print(data)
	return jsonify(**data)

@app.route("/justinify")
def justinify():
	data = reddit_request("http://www.reddit.com/r/puppies/hot.json")
	data = data["data"]["children"]
	list = []
	for i in range(0,len(data)):
		if not data[i]["data"]["stickied"]:
			title = data[i]["data"]["title"]
			url = data[i]["data"]["url"]
			position = i
			score = data[i]["data"]["score"]
			name = data[i]["data"]["name"]
			post = {
			"title": title,
			"url": url,
			"position": position,
			"score": score,
			"id": name
			}
			list.append(post)
	item = list[round(random.random()*(len(list)-1))]
	#print(item["url"][:16])
	#if item["url"][:16] == "http://imgur.com":
	
	#	url = imgur_url(item["url"])

	#return "<img src="+item["url"]+" alt=\"hi\"><p>"+item["title"]+"</p>"
	return jsonify(item)

@app.route("/add_event", methods="POST")
def data(d):
	name = request.form["name"]
	start = request.start["start"]
	end = request.form["end"]
	location = request.form["location"]
	description = request.form["description"]
	print(request.form)






if __name__ == "__main__":
	app.debug = True
	app.run()