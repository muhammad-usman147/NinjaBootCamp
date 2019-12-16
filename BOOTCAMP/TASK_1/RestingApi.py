from flask import Flask,jsonify
from firebase import firebase
app = Flask(__name__)

firebase = firebase.FirebaseApplication('https://ninjabootcamp-b7626.firebaseio.com/',None)


@app.route('/PutData/<title>/<desc>')
def Main(title,desc):
    
    data ={
        'Title':str(title),
        'Description':str(desc)
    }
    get_result = firebase.post('ninjabootcamp-b7626/',data)
    
    return jsonify(get_result)
@app.route("/getData")
def getdata():
    result = firebase.get('ninjabootcamp-b7626/','')
    return jsonify(result)
@app.route("/getData/<id>")
def GetParticularData(id):
    result = firebase.get('ninjabootcamp-b7626/',id)
    return jsonify(result)
@app.route("/UpdateData/<id>/<title>/<desc>")
def PutData(id,title,desc):
    result1 = firebase.put('ninjabootcamp-b7626/{}'.format(str(id)),'Title',title)
    result2=  firebase.put('ninjabootcamp-b7626/{}'.format(str(id)),'Description',desc)
    return str(bool(result2))
@app.route("/DeleteData/<id>")
def DeleteData(id):
    result1 = firebase.delete('ninjabootcamp-b7626/',id)
    return jsonify(result1)
if __name__ == "__main__":
    app.run(debug=True)