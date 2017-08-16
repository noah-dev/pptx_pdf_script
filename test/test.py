import os
import sys

import unittest
dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
pdf_path = os.path.join(dir_path, "src")
sys.path.insert(0,pdf_path)
import pdf

# For now, I am just testing whether or not it fails pdf.py files
# Not sure how to test watch.py yet. I will figure it out soon enough
class TestPDF(unittest.TestCase):

    def test_standard(self):
        infile = os.path.join(dir_path,"test/test.pptx")
        outfile = os.path.join(dir_path,"test/test.pdf")
        try: 
            pdf.pptx_to_pdf(infile, outfile)
        except:
            self.fail("pdf.py raised exception")

if __name__ == '__main__':
    unittest.main()