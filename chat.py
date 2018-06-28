from flask import Flask, render_template, request
import time

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/view', methods=["GET","POST"])
def view():
    if request.method == "POST":
        chat = request.form["user_input"]
        datetime = time.strftime('%m/%d %I:%M %p')
        message = str(request.remote_addr)+' ('+datetime+'): '+chat+'\n'
        latest = open('latest.txt','w')
        latest.write(message)
        latest.close()
        stuff = open('all.txt','a')
        stuff.write(message)
        stuff.close()
        stuff = open('history.txt','a')
        stuff.write(message)
        stuff.close()
    latest = open('all.txt', 'r')
    r=latest.readlines()
    p=['','','','','']
    for i in range(5):
       p[i] = r[len(r)-(i+1)]
    #message = latest.readlines()
    return render_template('view.html', text1 = p[4], text2 = p[3], text3 = p[2], text4 = p[1], text5 = p[0])+'testing'
    #return str(p)
    latest.close()

@app.route('/chat/<string:chat>')
def chat(chat: str):
    datetime = time.strftime('%m/%d %I:%M %p')
    message = str(request.remote_addr)+' ('+datetime+'): '+chat+'\n'
    latest = open('latest.txt','w')
    latest.write(message)
    latest.close()
    stuff = open('all.txt','a')
    stuff.write(message)
    stuff.close()
    stuff = open('history.txt','a')
    stuff.write(message)
    stuff.close()
    everything = open('history.txt','r')
    allstuff = everything.readlines()
    string = ''
    for i in range(len(allstuff)-1):
        string = string+allstuff[i]+'<br>'
    return string+'You chatted: '+chat
    everything.close()

@app.route('/', methods = ["POST","GET"])
def viewall():
    if request.method == "POST":
        chat = request.form["user_input"]
        datetime = time.strftime('%m/%d %H:%M:%S')
        message = str(request.remote_addr)+' ('+datetime+'): '+chat+'</></a>\n'
        latest = open('latest.txt','w')
        latest.write(message)
        latest.close()
        stuff = open('all.txt','a')
        stuff.write(message)
        stuff.close()
        stuff = open('history.txt','a')
        stuff.write(message)
        stuff.close()
    all = open('history.txt','r')
    allstuff = all.readlines()
    string = ''
    for i in range(len(allstuff)):
        string = string+allstuff[i]+'<br>'
    return '</p><p style="width:40%">'+string+'</p>'+render_template('viewall.html')
    #return string+'\n <meta http-equiv="refresh" content="2">'
    all.close()
@app.route('/clearall')
def clear():
    all = open('history.txt','w')
    all.write(str(request.remote_addr)+' cleared the chat at '+time.strftime('%m/%d %H:%M:%S')+'\n')
    all.close()
    return render_template('clearall.html')
@app.route('/everything')
def showall():
    all = open('all.txt','r')
    allstuff = all.readlines()
    string = ''
    for i in range(len(allstuff)):
        string = string+allstuff[i]+'<br>'
    return string
    all.close()

@app.route('/livefeed', methods = ["POST","GET"])
def livefeed():
    all = open('history.txt','r')
    allstuff = all.readlines()
    string = ''
    for i in range(len(allstuff)):
        string = string+allstuff[i]+'<br>'
    return string+'\n <meta http-equiv="refresh" content="1">'
    all.close()
    
if __name__ == "__main__":
    app.run(host = "10.80.0.255")
