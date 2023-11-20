from flask import Flask, request, jsonify
import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="root",
    database="testdatabase"
)

mycursor = db.cursor()

app = Flask(__name__)

@app.route("/")
def get_all():
    mycursor.execute("SELECT * FROM USER")

    # mycursor.fetchall()

    return jsonify(list(mycursor))

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Billy Strings",
        "email": "billy@bmfs.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    # you can use request.method if you are using multiple CRUD methods in the methods array above.
    # if request.method == "POST"
    # below we are taking in the json data passed in from the post request so that we are able to do something with it in this case just sending it back to the user.
    data = request.get_json()

    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)