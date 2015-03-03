Simple API with the endpoints:
----
Better documentation is here: http://api-workshop.readme.io/v1.0/docs

```
login: swsmith@bu.edu
password: nP?U6U7k}u
```

The absolute url is ```http://api.seanssmith.me/```

The API has the following relative endpoints:

* ```GET /``` -- returns version info and links to documentation
* ```GET /reddit``` -- returns some random JSON
* ```POST /reddit``` -- returns some random JSON given a reddit link and count
* ```GET /time``` -- returns current EST time in JSON format
* ```POST /addevent``` -- adds a calendar event of the following format

The ```/add_event``` adds an event with the following format:

```python
data = {
	"name": name,
	"start": start, 		 #start time
	"end": end,				 #end time
	"location": location,
	"description": description,

}
```

* ```GET /event``` -- gets the json of an event when you give it an id as a parameter
* ```DELETE /deleteevent``` -- deletes an event of the id passed as an argument
