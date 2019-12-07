from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/getUserData',methods=['POST'])
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
        return render_template("ShowData.html",x=data)
    elif flag == False:
        return render_template("ShowData.html",x=False)
if __name__ == '__main__':
    app.run(debug=True)