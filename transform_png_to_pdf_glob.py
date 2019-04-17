#! Python
# This is a program which converts PNG to PDF and merge them


from PIL import Image
import os, pytesseract, PyPDF2, reportlab, glob
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# locate the directory where the files are
user_folder = input('type the location where your image files are')
os.chdir(user_folder)


# loop through all image files
user_ask_extension = input('type the extension that you want to convert to pdf, for example png')
folders = glob.glob(user_folder)
imagenames_list = []
for folder in folders:
    for f in sorted(glob.glob(folder+'/*.'+user_ask_extension)):
        imagenames_list.append(f)

read_images = []
print(imagenames_list)

# extract text from the image files
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

user_pdf_name = input('type a name for your PDF file')
pdf_name = (user_pdf_name + '.pdf')
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
