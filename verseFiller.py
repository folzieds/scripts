from typing import List
import docx
import pandas as pd
import re


df_verse = pd.read_csv("verse.csv")

def get_text(filename: str) -> List:
    doc = docx.Document(filename)

    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)

    return full_text

def get_verse(full_text: List):
    found = []
    for text in full_text:
        if(re.search('[1-3]*\s[A-Za-z]*\s[1-9]*:\s[1-9]*\s-\s[1-9]*', text) != None):
            found.append(re.search('[1-3]*\s[A-Za-z]*\s[1-9]*:\s[1-9]*\s-\s[1-9]*', text))
        elif (re.search('[A-Za-z]*\s[1-9]*:\s[1-9]*\s-\s[1-9]*', text)) != None:
            found.append(re.search('[A-Za-z]*\s[1-9]*:\s[1-9]*\s-\s[1-9]*', text))
        elif(re.search('[1-3]*\s[A-Za-z]*\s[1-9]*:\s[1-9]*', text) != None):
            found.append(re.search('[1-3]*\s[A-Za-z]*\s[1-9]*:\s[1-9]*', text))
        elif (re.search('[A-Za-z]*\s[1-9]*:\s[1-9]*', text)) != None:
            found.append(re.search('[A-Za-z]*\s[1-9]*:\s[1-9]*', text))
        
    return found


x = get_text("test.docx")
y = get_verse(x)

for i in y:
    print(i)
