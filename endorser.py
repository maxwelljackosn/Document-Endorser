
""" This is a test """

from PyPDF2 import PdfFileWriter, PdfFileReader
from marisol import Marisol, Redaction, RedactionStyle, Area, StaticOverlay
from PyPDF2.pdf import PageObject




#Bates calculations
# M = Marisol('RFG', 6, 1)  # Begin numbering with RFG000001
# M.append('alpha.pdf')  # Path to PDF (1 page)
# doc = M[0]
# first_page = doc[0]
# location = (170, 300)  # offset from the left and bottom of the page.
# size = (100, 38)  # width and height of the redaction
# redaction = Redaction(location, size)  # create a plain redaction
# first_page.add_redaction(redaction)  # add the redaction to the page
# second_page = doc[1]
# another_redaction = Redaction(location, size, "For Attorneys Eyes Only", RedactionStyle.OUTLINE) # with text and a style
# second_page.add_redaction(another_redaction)
# print("done")

# M.save()  # save all documents
# doc = next(M)
# doc.save()  # save one document
# another_doc = next(M) 
# another_doc.save("customName.pdf")  # specify a custom file name



reader = PdfFileReader(open("Doc1.pdf", 'rb+'))
invoice_page = reader.getPage(0)
sup_reader = PdfFileReader(open("alpha.pdf",'rb+'))
sup_page = sup_reader.getPage(0)  # We pick the second page here

translated_page = PageObject.createBlankPage(None, sup_page.mediaBox.getWidth(), sup_page.mediaBox.getHeight())
translated_page.mergeScaledTranslatedPage(sup_page, 0.98, 0, 0)  # -400 is approximate mid-page

translated_page.mergePage(invoice_page)

writer = PdfFileWriter()
writer.addPage(translated_page)

with open('out.pdf', 'wb') as f:
	writer.write(f)
f.save()
