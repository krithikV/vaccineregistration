from flask import render_template, Flask, request
import pyrebase
import datetime as dt
import mae
import pulp
import mail as m
config = {
    "apiKey": "AIzaSyAewV4Rz46nxin8FNPj1yY_OJZ_rlMqg8c",
    "authDomain": "cowin-6421b.firebaseapp.com",
    "projectId": "cowin-6421b",
    "storageBucket": "cowin-6421b.appspot.com",
    "messagingSenderId": "369669481990",
    "appId": "1:369669481990:web:7dec3a3efb4a711896c587",
    "measurementId": "G-GD6T6XZC73",
    "databaseURL": "https://cowin-6421b-default-rtdb.firebaseio.com/"
  }
firebase = pyrebase.initialize_app(config)
db = firebase.database()
users = db.child("Places").get()
cityList = []
for i in users.each():
    cityList.append(i.key())
app = Flask(__name__)
@app.route("/")
def main():
    return render_template("index.html",cityList=cityList )
@app.route("/", methods=['POST'])
def register():
    name = request.form['name']
    dob = request.form['dob']
    tel = request.form['tel']
    email = request.form['email']
    id = request.form['id']
    place = request.form['place']
    key = db.generate_key()
    data = {'Name': name, 'DOB': dob , 'Tel': tel, 'Email':email, 'Govt ID': id, 'Centre': place, 'Key': key}
    db.child("Patients"+"/"+key).set(data)
    for i in cityList:
        if place == i:
            prepep = db.child("Places"+"/"+i+"/"+mae.get_part_of_day(dt.datetime.now().hour)).get()
            maxpep = db.child("Places"+"/"+i+"/"+mae.get_part_of_day(dt.datetime.now().hour)+"max").get()
            print(prepep.val())
            print(maxpep.val())
            if int(prepep.val()) < int(maxpep.val()):
                db.child("Places").child(i).update({mae.get_part_of_day(dt.datetime.now().hour): prepep.val()+1})
                m.notify(email, prepep.val()+1, name,mae.get_part_of_day(dt.datetime.now().hour), place)
    return render_template("index.html", cityList= cityList)


if __name__ == "__main__":
    app.run()
    pass