
""" This is a test """

from PyPDF2 import PdfFileWriter, PdfFileReader
from marisol import Marisol, Redaction, RedactionStyle, Area, StaticOverlay
from PyPDF2.pdf import PageObject


filename = "alpha.pdf"
endorsementtext = "Privileged"
endorsementtype = "Static"
batesfrom = 1
batesto = 6


def main():
    print("python main function")

    if (endorsementtype == "Static"):
        
        static()
        shrink()

    elif endorsementtype == "Bates":
            bates()
            shrink()
    else:
            print("Invalid Endorserment Type")
            return


def bates():
    
    M = Marisol('RFG', batesto, batesfrom)  # Begin numbering with RFG000001
    M.append(filename)  # Path to PDF (1 page)
    doc = M[0]
   
    first_page = doc[0]
    pdf = PdfFileReader(open(filename, 'rb+'))
    pdf.getNumPages()
    M.save()  # save all documents
    doc.save()  # save one document



def static():
    
    #Bates calculations

    M = Marisol('   ', 6, 1 )  # Begin numbering with RFG000001
    M.append(filename)  # Path to PDF (1 page)
    doc = M[0]
    location = (10, 10)  # offset from the left and bottom of the page.
    size = (200, 38)  # width and height of the redaction
    first_page = doc[0]
    pdf = PdfFileReader(open(filename, 'rb+'))
    pdf.getNumPages()
    
    # if(batesto < pdf.getNumPages()):
    #     print("Invalid bates numbers")

    # else: 
    #     print(pdf.getNumPages())
    #     # M.save()  # save all documents
    #     # doc.save()  # save one document

    i = 0
    while (i < pdf.getNumPages()):
            print(i)
        
            redaction = Redaction(location, size)  # create a plain redaction
            first_page.add_redaction(redaction)  # add the redaction to the page
            second_page = doc[i]
            another_redaction = Redaction(location, size, endorsementtext, RedactionStyle.OUTLINE) # with text and a style
            second_page.add_redaction(another_redaction)
            print("done")
            i += 1

    M.save()  # save all documents
    doc.save()  # save one document


def shrink():
    
    reader = PdfFileReader(open("Doc1.pdf", 'rb+'))
    invoice_page = reader.getPage(0)
    sup_reader = PdfFileReader(open(filename, 'rb+'))
    sup_page = sup_reader.getPage(0)  # We pick the second page here

    translated_page = PageObject.createBlankPage(None, sup_page.mediaBox.getWidth(), sup_page.mediaBox.getHeight())
    translated_page.mergeScaledTranslatedPage(sup_page, 0.98, 0, 0)  # -400 is approximate mid-page

    translated_page.mergePage(invoice_page)

    writer = PdfFileWriter()
    writer.addPage(translated_page)

    with open('out.pdf', 'wb') as f:
        writer.write(f)
    f.save()

    if f.save:
        print("Saved File Successfully")

    else:
        print("Failed for save file")





if __name__ == '__main__':
    main()
