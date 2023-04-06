#Importing all the necessary files

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
#Extracting the text from pdf
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
try:
    text1=(convert_pdf_to_txt('nb.pdf'))
    text2=(convert_pdf_to_txt('job_desc.pdf'))
except:
    print("Enter a file in a pdf format")
    pass 
#Extracting the applicant's details
tl=text1.split("\n")
name=tl[0]
mailID =[word for word in tl if re.search('[a-zA-Z0-9]@gmail|yahoo|outlook.com|co.in+',word)]
print("The name of the applicant: "+name.replace(" ",""))
print("\n")
print("The mail id of the applicant is "+mailID[0],end="\n")
print("\n")
#Converting the text to list
#vectorization work
content =[text2,text1]
countVector= CountVectorizer()
matrix = countVector.fit_transform(content)
#Checking the similarity with the help of cosine similarities
similarity_matrix=cosine_similarity(matrix)
#print(similarity_matrix)
result = ('Resume matches by:'+str(similarity_matrix[1][0]*100)+'%')
print(result)




