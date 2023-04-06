import pyrebase
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

# path of the json credentials
cred = credentials.Certificate('serviceAccountKey.json')

# initialize the firebase app
firebase_admin.initialize_app(cred, {
    "apiKey" : "AIzaSyCWYZxcRcK0ohsr465bnUufwLekND1EGPU",
    "authDomain" : "resume-parser-913c4.firebaseapp.com",
    "projectId" : "resume-parser-913c4",
    "storageBucket" : "resume-parser-913c4.appspot.com",
    "ServiceAccount" : "serviceAccountKey.json" ,
    "messagingSenderId" : "468299074766",
    "appId" : "1:468299074766:web:6088d4ec71cb6fe55f549f",
    "measurementId" : "G-59QNMLQ7XM",
    "databaseURL" : "https://resume-parser-913c4-default-rtdb.firebaseio.com"

})



# get the bucket
bucket = storage.bucket()

# create the folder where to store the files

# get all the files from the bucket
blobs = bucket.list_blobs()

# download all the files
for blob in blobs:
    filename = blob.name.split('/')[-1]
    print(filename)
    blob.download_to_filename(filename)
 

