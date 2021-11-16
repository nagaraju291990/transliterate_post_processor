import sys
import re
import os
from argparse import ArgumentParser

parser = ArgumentParser(description='To handle nukta issue in Devnagari output of Urdu2Hindi Transliteration \n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=inputfie"
						)
parser.add_argument("-i", "--input", dest="inputfile",
                    help="provide .txt file name",required=True)

args = parser.parse_args()

inputfile = args.inputfile

#open input file using open file mode
fp1 = open(inputfile, encoding="utf-8") # Open file on read mode
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

for line in lines:
    #src_word = line.split("\t")[0]
    #tgt_word = line.split("\t")[1]
    if(re.search(r'ق', line) and re.search(r'क', line)):
        line = re.sub(r'क', 'क़', line)
    if(re.search(r'خ', line) and re.search(r'ख', line)):
        line = re.sub(r'ख', 'ख़', line)
    if(re.search(r'غ', line) and re.search(r'ग', line)):
        line = re.sub(r'ग', 'ग़', line)
    if(re.search(r'[ذ ز ژضظ]', line) and re.search(r'ज', line)):
        line = re.sub(r'ज', 'ज़', line)
    if(re.search(r'ف', line) and re.search(r'फ', line)):
        line = re.sub(r'फ', 'फ़', line)
    if(re.search(r'ح', line) and re.search(r'ह', line)):
        line = re.sub(r'ह', 'ह़', line)

    line = re.sub(r'़+','़', line)
    print(line)