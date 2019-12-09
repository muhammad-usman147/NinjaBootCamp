from flask import Flask,render_template,request,redirect,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/getUserData',methods=['GET','POST'])
def GetData():

    flag = True
    data = dict(request.form)
    print(bool(data),data)
    for i,v in data.items():
        print("Running")
        if bool(v) == False:
            flag = False
            break
        elif bool(v) == True:
            pass
    if flag == True:
        
        data['id'] = '1213412'
        data['title'] = 'empty title'
        data['description'] = 'empty description'        
        return jsonify(data)
    elif flag == False:
        data['id'] = '1213412'
        data['title'] = 'empty title'
        data['description'] = 'empty description'
        return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True)