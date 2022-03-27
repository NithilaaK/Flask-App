from flask import Flask, jsonify, request
app = Flask(__name__)
contacts = [
    {
        "id":1,
        "name":u"Raju",
        "contact":u"9987644456",
        "done":False
    },
    {
        "id":2,
        "name":u"Rahul",
        "contact":u"9876543222",
        "done":False
    }
]
@app.route("/add-data", methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"ERROR",
            "message":"Please provide data."
        }, 400)
    contact = {
        "id":contacts[-1]["id"]+1,
        "name":request.json["title"],
        "description":request.json.get('description', ""),
        "done":False
    }
    contacts.append(contact)
    return jsonify({
        "status":"SUCCESS",
        "message":"Contact successfully added."
    })
@app.route("/get-data")
def get_contact():
    return jsonify({
        "data":contacts
    })
if (__name__=="__main__"):
    app.run(debug=True)