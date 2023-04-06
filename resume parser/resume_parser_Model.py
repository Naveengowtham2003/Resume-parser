#!/usr/bin/env python
# coding: utf-8



#Importing all the necessary libraries
import pyrebase
from nltk import word_tokenize
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import docx2txt
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import pandas as pd
import spacy
from spacy.matcher import Matcher
from operator import itemgetter
from nltk.corpus import stopwords

import os
import nltk
nltk.download('words')


# In[27]:


folder_path ="D:/Naveen/resume parser/resume"
files_list = os.listdir(folder_path)
#Iterate over all the files

for filename in files_list:
    def convert_pdf_to_txt(FN):
        prm = PDFResourceManager()
        sio = StringIO()
        laparams = LAParams()
        tc = TextConverter(prm, sio, codec='utf-8', laparams=laparams)
        fp = open(FN, 'rb')
        interpreter = PDFPageInterpreter(prm, tc)
        password = ""
        maxpages = 0
        caching = True
        pagenos=set()
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)
        text = sio.getvalue()
        fp.close()
        tc.close()
        sio.close()
        return text

    def extract_text_from_doc(doc):
        temp = docx2txt.process("doc")
        text = [line.replace('\t', ' ') for line in temp.split('\n') if line]
        return ' '.join(text)
     #get the file name

    name, ext = os.path.splitext(filename)
    if ext == ".pdf":
        try:
            text1=(convert_pdf_to_txt(filename))
            text2=(convert_pdf_to_txt('job_desc.pdf'))
            print("............................Text Extracted from pdf....................")
        except:
            print("Oops! unable to wrap the text")
        pass

    elif(ext=='.doc'):
        try:
            text1=(convert_pdf_to_txt('myresume.pdf'))
            text2=(convert_pdf_to_txt('job_desc.pdf'))
            print("............................Text Extracted from pdf....................")
        except:
            print("Oops! unable to wrap the text ")
            print(None)
            pass

    elif(ext=='.txt'):
        print("This model is capable of extracting text from '.txt' files as well but due to some layout issues it is not preferable it may leads to wrong prediction/extraction 'Enter 'Yes'to continue'.")
        yn=input("Yes/no").lower()
        try:
            with open('countries.txt','r') as file:
                text1 = file.read()
                print("............................Text Extracted from pdf....................")
        except:
            print("Oops! unable to wrap the text ")
            pass
    else:
        print("pdf is not in any of the supported form kindly enter any of the supported forms or else chek your file")
        pass
    #print(text1)


    #Extracting Name from the Resume
    nlp = spacy.load('en_core_web_sm')
    matcher = Matcher(nlp.vocab)

    def extract_name(resume_text):
        nlp_text = nlp(resume_text)
        # First name and Last name are always Proper Nouns
        pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
        matcher.add('NAME',[pattern])
        matches = matcher(nlp_text)
        for match_id, start, end in matches:
            span = nlp_text[start:end]
            return span.text
    tl= text1.split("\n")

    def mail_extr(text):
        mailID =[word for word in tl if re.search('[a-zA-Z0-9]@gmail|yahoo|outlook.com|co.in+',word)]
        if mailID:
            try:
                return mailID[0]
            except IndexError:
                return None

    def phono_extr(text):
        phno=re.findall('\d{3}\d{3}\d{4}',text)
        if len(phno[0])<10:
            return None
        else:
            return phno[0]

    def linkedin_extr(text):
        lnurl=re.findall('(https?:\/\/(www\.)?linkedin\.com\/in\/[a-zA-Z0-9-]+)',text)
        ln=" "
        for i in lnurl:
            ln=i[0]
            return ln

    def extract_skills(text):
        print(text)

    name=(extract_name(text1))
    phone_No=(phono_extr(text1))
    mail_Id=(mail_extr(text1))
    linked_In_Id=(linkedin_extr(text1))

    #Computing Cosine similarity
    def cos_compute(text1,text2):
        content =[text2,text1]
        countVector= CountVectorizer()
        matrix = countVector.fit_transform(content)
        similarity_matrix=cosine_similarity(matrix)
        return ('Resume matches by:'+str(round((similarity_matrix[1][0]),2)*100)+ ' % to that of given job description')
    if (name is not None):
        print("Name of the applicant is:"+name+"\n")

    if (mail_Id is not None):
        print("Mail_Id of the applicant is:"+mail_Id+"\n")
    else:
        pass

    if (phone_No is not None):
        print("Phone Number the applicant is:"+phone_No+"\n")
    else:
        pass

    if (linked_In_Id is not None):
        print("Linked in URL of the applicant is:"+linked_In_Id+"\n")
    else:
        pass
    percentage = (cos_compute(text1,text2))
    print(percentage)



# In[14]:




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



data = {"Name": name, "Email_id": mail_Id, "Phone_No": phone_No, "Linked_In": linked_In_Id, "Percentage": percentage}

database.child("resume_selected_names").child(name).set(data)