import sys
import os
import pdf
import time

# Read in system arguments 
# eg. C:\apps\active\vml\ppt_archive_script\docs\issues.pptx
if len(sys.argv) == 2:
    print("Please state the file name of the PPTX")
    sys.exit()
# Read in arguments - if only input filename given, copy for output filename
infile = sys.argv[2]
if len(sys.argv) == 3:
    outfile = infile[:-5] + ".pdf"
else:
    outfile = sys.argv[3][:-5] + ".pdf"

# See if file is absolute
if not os.path.isabs(infile):
    infile = os.path.join(os.getcwd(), infile)
    outfile = os.path.join(os.getcwd(), outfile)
# See if file is valid
if os.path.isfile(infile) and infile[-4:]=="pptx":
    print("PPT located at ", infile)
else:
    print("PPT at"+infile+", does not exist")
    sys.exit()

# Polling - not elegant but straight forward
last_modified = 0; 
while True:
    now = os.stat(infile).st_mtime
    if now != last_modified:
        # If the modified date is different from previously recorded, update
        pdf.pptx_to_pdf(infile, outfile)
        last_modified = now
        print("PPT published at ", outfile)
    else:
        # Otherwise just sleep
        time.sleep(1)
