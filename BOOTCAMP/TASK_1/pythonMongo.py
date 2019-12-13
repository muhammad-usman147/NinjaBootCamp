from flask import Flask, jsonify
from pymongo import MongoClient
monngo = MongoClient('mongodb+srv://test:test@cluster0-onecv.mongodb.net/test?retryWrites=true&w=majority')

#creating Cliet
app = Flask(__name__)
db = monngo.get_database('UsmanDataBase')
collection = db.collection_no1

@app.route('/')
def Main():
    return "hello world"

#GET API FULL
@app.route('/GetData',methods=['GET'])
def GetAllData():
    data = collection.find()
    ls = []
    print(type(data))
    for i in data:
        i.pop('_id')
        ls.append(i)
    return jsonify(ls)
#GET API FOR SINGLE RECORD
@app.route('/GETSINGLEDATA/<idx>')
def GetSingleData(idx):
    x = collection.find_one({"id":idx})
    data = {}
    for i,v in x.items():
        if i != '_id':
            data[i] = v
    print(data)
    return jsonify(data)
#POST API
@app.route('/POSTDATA/<id>/<title>/<desc>/<done>',methods=['POST'])
def PostData(id,title,desc,done):
    data = {
        'id':id,
        'title':title,
        'description':desc,
        'done':done
    }
    x  = collection.insert_one(data)
    if x:
        return jsonify({'RESULT':'TRUE'})
    else:
        return jsonify({"RESULT":"FALSE"})

#UPDATE API -- PUT
@app.route('/UPDATEDATA/<id>/<key>/<value>',methods=['PUT'])
def UpdateData(id,key,value):
    update_data = {key:value}
    x = collection.update_one({'id':id},{'$set':update_data})
    if x:
        return jsonify({'RESULT':'TRUE'})
    else:
        return jsonify({"RESULT":"FALSE"})
#DELETE API --DELETE
@app.route("/DELETEDATA/<id>",methods=['DELETE'])
def DeleteDAta(id):
    x = collection.delete_one({'id':id})
    if x:
        return jsonify({'RESULT':'TRUE'})
    else:
        return jsonify({"RESULT":"FALSE"})
if __name__ == "__main__":
    app.run(debug=True)