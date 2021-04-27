import os
import PyPDF2
from gtts import gTTS
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
file_location = askopenfilename()

with open(file_location, "rb") as f:
    pdf = PyPDF2.PdfFileReader(f)
    myText = " "
    for pageNum in range(pdf.numPages):
        pageObj = pdf.getPage(pageNum)
        myText += pageObj.extractText()
print(myText)

final_output = gTTS(text=myText, lang='en')
print("Generating Speech.....")
final_output.save("Generated_Speech.mp3")
os.system("Start Generated_Speech.mp3")

print("Successfully Generated!!")

