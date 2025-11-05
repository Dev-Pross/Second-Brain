import pypdf
from pathlib import Path
from docx import Document


def parse_pdf(file_path):
    """Extract text from PDF file"""
    reader = pypdf.PdfReader(str(file_path))
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


def parse_docx(file_path):
    """Extract text from DOCX file"""
    document = Document(str(file_path))
    text = "\n".join([paragraph.text for paragraph in document.paragraphs])
    return text


def parse_document(file_path):
    """Parse PDF or DOCX - auto-detects file type"""
    path = Path(file_path)
    suffix = path.suffix.lower()
    
    if suffix == '.pdf':
        return parse_pdf(path)
    elif suffix == '.docx':
        return parse_docx(path)
    else:
        raise ValueError(f"Unsupported file type: {suffix}. Use .pdf or .docx")
    

def chunk_words(text, chunk_size, overlap=50):
    words = text.split()
    if chunk_size <= 0:
        raise ValueError("chunk_size must be > 0")
    # ensure overlap is non-negative and smaller than chunk_size
    overlap = max(0, min(overlap, chunk_size - 1))
    step = chunk_size - overlap

    chunks = []
    for i in range(0, len(words), step):
        chunk = ' '.join(words[i:i + chunk_size])
        if len(chunk) > 50:
            chunks.append(chunk)

    return chunks

if __name__ == "__main__":
    # Test with your PDF file
    test_file = "HOW PEOPLE USE CHATGPT.pdf"
        chunks = chunk_words(text, 60, 50)
        # print("The chuncks are",chunks)
        text = parse_document(test_file)
        print(f"✅ Successfully extracted {len(text)} characters")
        print(f"First 200 characters:\n{text[:200]}")
        chunks = chucnk_words(text, 60, 50)
        # print("The chuncks are",chunks)
    except FileNotFoundError:
        print(f"❌ File not found: {test_file}")
    except Exception as e:
        print(f"❌ Error: {e}")
