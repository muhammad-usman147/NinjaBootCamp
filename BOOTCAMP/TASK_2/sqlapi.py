from flask import Flask,jsonify
import sqlite3 as sq


'''
conn = sq.connect("testing.db")
    #creating database file with the name UsmanDataBase
c = conn.cursor()

#this is my table name
c.execute(""" CREATE TABLE TODO ( 
    id integer,
    title text,
    description text,
    done text
    ) """)
conn.commit()


'''
app = Flask(__name__)

@app.route("/api/get",methods=['GET'])
def getapi():
    conn = sq.connect("testing.db")
    #creating database file with the name UsmanDataBase
    c = conn.cursor()
    c.execute("SELECT * FROM TODO ")
    data = c.fetchall()
    print(data)
    if data:
        return jsonify({'RESULT':data})
    else:
        return jsonify({"RESULT":None})

@app.route("/api/singleget/<ids>",methods=['GET'])
def SingleGet(ids):
    conn = sq.connect("testing.db")
    #creating database file with the name UsmanDataBase
    c = conn.cursor()
    c.execute("SELECT * FROM TODO WHERE id = ?",(ids,))
    data = c.fetchall()
    if data:
        return jsonify({'RESULT':data})
    else:
        return jsonify({"RESULT":None})

@app.route("/api/post/<ids>/<title>/<desc>/<done>",methods=['POST'])
def postapi(ids,title,desc,done):
    ids = ids
    title = title
    desc = desc
    done = done
    conn = sq.connect("testing.db")
    #creating database file with the name UsmanDataBase
    c = conn.cursor()
    result = c.execute("INSERT INTO TODO VALUES(?,?,?,?)",(ids,title,desc,done))
    conn.commit()
    if result:
        return jsonify({'RESULT':"DATA inserted"})
    else:
        return jsonify({"RESULT":None})
@app.route("/api/put/<ids>/<title>/<value>",methods=['PUT'])
def put(ids,title,value):
    conn = sq.connect("testing.db")
    #creating database file with the name UsmanDataBase
    c = conn.cursor()
    result = c.execute("UPDATE TODO SET title=? where id =? ",(value,ids))
    conn.commit()
    if result:
        return jsonify({"RESULT":"UPADATED"})
    else:
        return jsonify({"RESULT":None})
@app.route("/api/delete/<ids>",methods=['DELETE'])
def Delete(ids):
    conn = sq.connect("testing.db")
    #creating database file with the name UsmanDataBase
    c = conn.cursor()
    result = c.execute("DELETE FROM TODO WHERE id =(?) ",(ids,))
    conn.commit()
    if result:
        return jsonify({"RESULT":"UPADATED"})
    else:
        return jsonify({"RESULT":None})
        
if __name__ == "__main__":
    app.run(debug=True,port=5008)
