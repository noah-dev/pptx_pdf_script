# https://stackoverflow.com/questions/31487478/how-to-convert-a-pptx-to-pdf-using-python

import comtypes.client

def PPTtoPDF(inputFileName, outputFileName, formatType = 32):
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1

    if outputFileName[-3:] != 'pdf':
        outputFileName = outputFileName + ".pdf"
    deck = powerpoint.Presentations.Open(inputFileName)
    deck.SaveAs(outputFileName, formatType) # formatType = 32 for ppt to pdf
    deck.Close()
    powerpoint.Quit()

infile = "../docs/issues.pptx"
outfile = "../docs/issues.pdf"
PPTtoPDF(infile, outfile)