import comtypes.client
import os

def export_deck(powerpoint, inputFileName, outputFileName, formatType = 32):
    deck = powerpoint.Presentations.Open(inputFileName)
    deck.SaveAs(outputFileName, formatType) 
    deck.Close()

def pptx_to_pdf(inputFileName, outputFileName, formatType = 32):
    ''' Using absolute path, pass input file name and output file name
        Based on: https://stackoverflow.com/questions/31487478/how-to-convert-a-pptx-to-pdf-using-python
    '''
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1

    if outputFileName[-3:] != 'pdf':
        outputFileName = outputFileName + ".pdf"
    
    # Check to see if powerpoint file is already open
    try: 
        # If it works, then assuming the file is not open
        test = open(inputFileName, "r+")
        test.close()
        export_deck(powerpoint, inputFileName, outputFileName, formatType = 32)
        powerpoint.Quit()
    except:
        # If it does not raise an exception, then the file is already open. 
        # In which case, do not close out of the powerpoint after saving as pdf
        export_deck(powerpoint, inputFileName, outputFileName, formatType = 32)
        