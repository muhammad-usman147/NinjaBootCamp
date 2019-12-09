from flask import Flask,jsonify
from firebase import firebase
app = Flask(__name__)

firebase = firebase.FirebaseApplication('https://ninjabootcamp-b7626.firebaseio.com/',None)


@app.route('/')
def Main():
    
    data ={
        'Title':'Machine Learning Enginner',
        'Description':"Currently Working as in NASA"
    }


    result = firebase.get('ninjabootcamp-b7626/BootCampTable1','')
    print("--------------------")
    print(result['-LvfcXHBVbNiclUCMXQl']['Description'])
    print("--------------------")
    print(result['-LvfcXHBVbNiclUCMXQl']['Title'])
    return jsonify(result)
if __name__ == "__main__":
    app.run(debug=True)