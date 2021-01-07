# race_db
# Required
flask
flask_restful
SQLAlchemy
flask_jsonpify

# Implementation
```bash
python api.py
```
then go to the specified port.\
Example queries:
http://127.0.0.1:5002/byType/Next+to+jump

returns all Next to jump races with their attributes.

Other types: see race_type.csv

# Development details
For this problem, first I create a database using sqlite3 in python:
- define an entity diagram: I come up with 3 entities: Race type, Race venue, Race
- create a toy database based on this entity diagram:
	- create 3 tables
	- read 3 csv files
	and insert their content into 3 tables defined above

Next, I define how end user can perform `SELECT` query with the parameter `Race type`. I simply construct a `get` method for this purpose.


