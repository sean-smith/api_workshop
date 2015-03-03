
from flask import Flask, jsonify, request
import time, requests, random,json, hashlib, redis
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
	"Name": "Sean's API",
	"URL": "https://github.com/sean-smith/api_workshop",
	"Gist": "https://gist.github.com/sean-smith/b6230be9f6dd900d6209"
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

@app.route("/reddit", methods =["POST", "GET"])
def justinify():
	if request.method == "GET":
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
		if request.args.get("position") != None:
			c = int(request.args.get("position"))
			item = list[c]
		else:
			item = list[round(random.random()*(len(list)-1))]
		if request.args.get("html") == "True":
			print(item["url"][:16])
			return "<img src="+item["url"]+" alt=\"hi\"><p>"+item["title"]+"</p>"
		return jsonify(**item)
	if request.method == "POST":
		uri = request.form["url"]
		c = int(request.form["position"])
		data = reddit_request(uri+".json")
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
		item = list[count]
		return jsonify(**item)

@app.route("/addevent", methods=["POST"])
def data():
	name = request.form["name"]
	start = request.form["start"]
	end = request.form["end"]
	location = request.form["location"]
	description = request.form["description"]
	data = {
	"name": name,
	"start": start, 		 #start time
	"end": end,				 #end time
	"location": location,
	"description": description,
	}
	h = hashlib.md5(str(data).encode("utf-8"))
	status = r.set(h.hexdigest(), json.dumps(data))
	response = {
	"id": h.hexdigest(),
	"completed": status
	}
	return jsonify(**response)

@app.route("/event", methods=["GET"])
def get():
	i = str(request.args.get("id"))
	response = r.get(i)
	if response != None:
		return response
	else:
		return jsonify(**{"ERROR":"Invalid Key"})


@app.route("/deleteevent", methods=["DELETE"])
def delete():
	i = str(request.args.get("id"))
	response = r.delete(i)
	if response != None:
		return jsonify(**{"worked":response})
	else:
		return jsonify(**{"ERROR":"Invalid Key"})

if __name__ == "__main__":
	r = redis.StrictRedis(host='54.191.86.186', port=6379, db=1)
	app.run(debug = True)
	#app.run(host = '0.0.0.0', port=80)