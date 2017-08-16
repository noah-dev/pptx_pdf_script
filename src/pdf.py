import comtypes.client
import os

def PPTtoPDF(inputFileName, outputFileName, formatType = 32):
    ''' Using absolute path, pass input file name and output file name
        Based on: https://stackoverflow.com/questions/31487478/how-to-convert-a-pptx-to-pdf-using-python
    '''
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1

    if outputFileName[-3:] != 'pdf':
        outputFileName = outputFileName + ".pdf"
    deck = powerpoint.Presentations.Open(inputFileName)
    deck.SaveAs(outputFileName, formatType) # formatType = 32 for ppt to pdf
    deck.Close()
    powerpoint.Quit()