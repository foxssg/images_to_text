#! Python
# This is a program which converts PNG to PDF and merge them


from PIL import Image
import os, pytesseract, PyPDF2, reportlab, glob
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# locate the directory where the files are
os.chdir("/home/foxs/Downloads/pysheng-master/LuciusAnnaeusSeneca")


# loop through all PNG files       
folders = glob.glob("/home/foxs/Downloads/pysheng-master/LuciusAnnaeusSeneca")
imagenames_list = []
for folder in folders:
    for f in sorted(glob.glob(folder+'/*.png')):
        imagenames_list.append(f)

read_images = []
print(imagenames_list)

# extract text from PNG
for image in imagenames_list:
    Image.open(image)
    read_images.append(pytesseract.image_to_string(image, lang='eng'))
    print(image)
    print(read_images)
str1 = ''.join(read_images)

# creating and saving text to PDF
styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']
story = []

pdf_name = 'your_pdf_file.pdf'
doc = SimpleDocTemplate(
    pdf_name,
    pagesize=letter,
    bottomMargin=.4 * inch,
    topMargin=.6 * inch,
    rightMargin=.8 * inch,
    leftMargin=.8 * inch)

text_content = str1

P = Paragraph(text_content, styleN)
story.append(P)

doc.build(
    story,
)
