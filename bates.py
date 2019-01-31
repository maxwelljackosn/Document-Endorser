
from PyPDF2 import PdfFileWriter, PdfFileReader
from marisol import Marisol, Redaction, RedactionStyle, Area, StaticOverlay
from PyPDF2.pdf import PageObject


#Bates calculations
M = Marisol('RFG', 6, 1)  # Begin numbering with RFG000001
M.append('./out.pdf')  # Path to PDF (1 page)
#first_page = doc[0]
# location = (170, 300)  # offset from the left and bottom of the page.
size = (100, 38)  # width and height of the redaction
#redaction = Redaction(Area.TOP_LEFT, size, "For Attorneys Eyes Only", RedactionStyle.OUTLINE)  # create a plain redaction
#first_page.add_redaction(redaction)  # add the redaction to the page
# second_page = doc[1]
#another_redaction = Redaction(Area.BOTTOM_RIGHT, size, "For Attorneys Eyes Only", RedactionStyle.OUTLINE) # with text and a style
#second_page.add_redaction(another_redaction)
try:
    overlay = StaticOverlay("CONFIDENTIAL", Area.BOTTOM_LEFT)
    doc = M[0]
    doc.add_overlay(overlay)


    print("done")

    M.save()  # save all documents
    doc = next(M)
    doc.save()  # save one document
except:
    print("It didnt work")