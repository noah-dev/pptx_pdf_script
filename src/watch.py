import sys
import os
import pdf
import time

# Read in system arguments 
# eg. C:\apps\active\vml\ppt_archive_script\docs\issues.pptx

if len(sys.argv) == 1:
    print("Please state the file name of the PPTX")
    sys.exit()
# Read in arguments - if only input filename given, copy for output filename
infile = sys.argv[1]
if len(sys.argv) == 2:
    outfile = infile[:-4] + ".pdf"
else:
    outfile = sys.argv[2]

# See if file is absolute
if not os.path.isabs(infile):
    infile = os.path.join(os.getcwd(), infile)
    outfile = os.path.join(os.getcwd(), outfile)
# See if is valid
if os.path.isfile(infile):
    print("PPT located...")
else:
    print("PPT at"+infile+", does not exist")

last_modified = 0; 
while True:
    now = os.stat(infile).st_mtime
    if now != last_modified:
        pdf.PPTtoPDF(infile, outfile)
        last_modified = now
        print("PPT Published")
    else:
        time.sleep(1)
