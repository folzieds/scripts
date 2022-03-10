import docx

def get_text(filename):
    doc = docx.Document(filename)

    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)

    return "\n\n".join(full_text)

test = input("Enter file name:")
file_text = get_text(test)

print(file_text)