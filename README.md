This is a Simple FLASK API with the following endpoints:
===============================================

GET /justinify -- returns some interesting JSON
GET /time -- returns current EST time in JSON
POST /add_event -- adds a calendar event of the following format

data = {
	"name": name,
	"start": start, 		 #start time
	"end": end,				 #end time
	"location": location,
	"description": description,

}

