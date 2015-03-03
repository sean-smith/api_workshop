import requests, json, random
from flask import jsonify
import xml.dom.minidom as parse


#Example Head request
r = requests.head("http://127.0.0.1:5000/")

print(r.headers)

#Example Post request
event = {
	"name": "name",
	"start": "start",
	"end": "end",
	"location": "loc",
	"description": "desc"
}

r = requests.post("http://127.0.0.1:5000/addevent", data=event)

print(r, r.content)


#Example get request

id = r.json()["id"]

r = requests.get("http://127.0.0.1:5000/event?id="+id)

print(r, r.content)

#Example delete request

r = requests.delete("http://127.0.0.1:5000/deleteevent?id="+id)

print(r, r.content)




