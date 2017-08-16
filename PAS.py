import comtypes.client
import os
import sys

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

# Read in system arguments 
# eg. C:\apps\active\vml\ppt_archive_script\docs\issues.pptx
infile = sys.argv[1]
outfile = sys.argv[2]
if os.path.isfile(infile):
    PPTtoPDF(infile, outfile)
    print("PPT located and PDF published")
else:
    print("PPT at"+infile+", does not exist")