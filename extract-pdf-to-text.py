# Install NLTK Data
from unstructured.partition.pdf import partition_pdf

def pdf_to_text(pdf_path):
    text = partition_pdf(pdf_path)
    return text

pdf_path = './A1860-45.pdf'
text = pdf_to_text(pdf_path)
text = "\n".join([str(el) for el in text])

output_file = './IPC.txt'
with open(output_file, 'w') as file:
    file.write(text)
