import docx
import pandas as pd

def get_text(filename):
    doc = docx.Document(filename)

    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)

    return "\n\n".join(full_text)

def get_verse(full_text):
    pd.read_csv("")