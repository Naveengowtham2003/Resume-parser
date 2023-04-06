import pyrebase
import os

config = {
    "apiKey" : "AIzaSyCWYZxcRcK0ohsr465bnUufwLekND1EGPU",
    "authDomain" : "resume-parser-913c4.firebaseapp.com",
    "projectId" : "resume-parser-913c4",
    "storageBucket" : "resume-parser-913c4.appspot.com",
    "messagingSenderId" : "468299074766",
    "appId" : "1:468299074766:web:6088d4ec71cb6fe55f549f",
    "measurementId" : "G-59QNMLQ7XM",
    "databaseURL" : "https://resume-parser-913c4-default-rtdb.firebaseio.com",
    "serviceAccount" : "serviceAccountKey.json"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
database = firebase.database()


data = database.child('resume_name').get()
result = data.val()
print(result)

ans = "applicant/"+result
print(ans)
storage.child("applicant/signature.jpg").download(path = "gs://resume-parser-913c4.appspot.com/", filename = "new.jpg")











