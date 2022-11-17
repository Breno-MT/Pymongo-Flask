# RESTful API Pymongo Flask

# About 🔰
- This API is made on Flask, Python and MongoDB Atlas.
- The objective of this API is to store Movies and Comments about it in an online NoSQL cloud based.

# Usage
- Must have Python 3.9+
- Must have MongoDB Compass
- Must have MongoDB Cloud configurated.

# How to use it
- Follow the .env_example and create a .env file.
- Install your own virtual env such as Poetry, Python env or etc...
- Then you simply activate your env:
```
python -m venv venv_name
source venv_name/bin/activate - Linux
venv_name/Scripts/activate.bat - Windows

Now install the requirements.txt
pip install -r requirements.txt

```
## After that just run:
```
flask create_collections
flask run
```
## After creating the collection follow the example below:
```
Add all the files on src/app/db/ in your MongoDB Compass,
Open your MongoDB Compass, go to one of the collection: comments or movies,
Then go on ADD DATA, Import File, Json, and select comments.json or movies.json from src/app/db/

doc: https://www.mongodb.com/docs/compass/current/documents/insert/
```
## Done! You're set to go!
- Ps: This project is WIP, so expect bugs, flaws etc...
