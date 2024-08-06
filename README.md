# validmoves
## Start server
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch server
# If nothing else is running on port 5000
flask run

# If you are running another flask server you will have to override the port. for example
flask run --port=31337

