import requests, json, random
from flask import jsonify
import xml.dom.minidom as parse


#Example Head request
r = requests.head("http://127.0.0.1:5000/")

print(r.headers)


#Example get request



#Example Post request
data = {
	"name": "name",
	"start": "start",
	"end": "end",
	"location": "loc",
	"description": "desc"
}

r = requests.post("http://127.0.0.1:5000/add_event", data)

print(r, r.content)

