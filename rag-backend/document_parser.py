import pypdf
from docx import Document
def pdf_parser(file_path):
    reader = pypdf.PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text 

def docx_parser(file_path):
    document = Document(str(file_path))
    text = "\n".join(paragraph.text for paragraph in document.paragraphs)
    return text 

def final_parser(file_path):
    if file_path.endswith(".pdf"):
        return pdf_parser(file_path)
    if file_path.endswith(".docx"):
        return docx_parser(file_path)
# file_path = "/home/vamsi/Projects/WEB DEV/second-brain/rag-backend/HOW PEOPLE USE CHATGPT.pdf"

file_path = "/home/vamsi/Projects/WEB DEV/second-brain/rag-backend/__VAMSI SARAGADMA VAMSHI__.docx"
if __name__ == "__main__":
    text = final_parser(file_path)
    # text = pdf_parser(file_path)
    print(text)
    # print("Hello word")

    print("Parsing the text form the given docuemt")
    print(file_path)

