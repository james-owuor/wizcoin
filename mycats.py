#cats=[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]
import os, shutil
def pdf_search(folder):
    folder= os.path.abspath(folder)
while True:
    PdfFilename= os.path.basename(folder)+ ".pdf"
    if not os.path.exists(folder):
        break
    for foldername, subfolders,filenames in os.walk(folder):
        print("The current folder is:"+ foldername)
    for subfolder in subfolders:
        print("The subfolder of" + foldername + ":"+ subfolders)
    for filename in filenames:
        newBase= os.path.basename(folder)+ "_"
    if  filename.startswith(newBase) and filename.endswith(".pdf"):
        continue
pdf_search("C:\\Users\\colli\\OneDrive\\Desktop")