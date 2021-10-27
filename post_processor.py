#program to find and replace characters/words from machine generated transliterated text
import sys
import re
import os
#import replace_list   #custom import file for word replacement
from argparse import ArgumentParser

parser = ArgumentParser(description='to find and replace characters/words from machine generated transliterated text \n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=inputfie" + " -l=y|n"
						)

parser.add_argument("-i", "--input", dest="inputfile",
					help="provide .txt file name",required=True)
parser.add_argument("-r", "--replace", dest="replaceFlag",
					help="replace anywhere in the string",required=False)
parser.add_argument("-l", "--listfile", dest="listfile",
					help="specify a list file that has tab seperated content", required=True)
parser.add_argument("-o", "--outfile", dest="outfile",
					help="specify output file name", required=True)

args = parser.parse_args()

inputfile = args.inputfile
listfile = args.listfile
replaceFlag = args.replaceFlag
outfile = args.outfile
#open input file using open file mode
fp1 = open(inputfile, encoding="utf-8") # Open file on read mode
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

#open list file using open file mode
fp2 = open(listfile, encoding="utf-8") # Open file on read mode
words = fp2.read().split("\n") # Create a list containing all lines
fp2.close() # Close file

six_word_hash = {}
five_word_hash = {}
four_word_hash = {}
three_word_hash = {}
two_word_hash = {}

word_hash = {}
all_hash = {}


#read list file into multiple hashes
for word in words:
	if(word != ""):
		col12 = word.split("\t")
		if(len(re.findall(" ", col12[0])) == 5 ):
			six_word_hash[col12[0]] = col12[1]
		elif(len(re.findall(" ", col12[0])) == 4 ):
			five_word_hash[col12[0]] = col12[1]
		elif(len(re.findall(" ", col12[0])) == 3 ):
			four_word_hash[col12[0]] = col12[1]
		elif(len(re.findall(" ", col12[0])) == 2 ):
			three_word_hash[col12[0]] = col12[1]
		elif(len(re.findall(" ", col12[0])) == 1 ):
			two_word_hash[col12[0]] = col12[1]
		else:
			word_hash[col12[0]] = col12[1]

for d in (six_word_hash, five_word_hash, four_word_hash, three_word_hash, two_word_hash, word_hash):
	all_hash.update(d)

keys = all_hash.keys()

#read input file line by line and replace with hash match values
k = 0
i = 0
#out = []
kl = len(keys)-1
#for line in lines:
for key in keys:
	i = 0

	for line in lines:

		#character replacement of o to danda
		line = re.sub(r'o', '। ', line, flags = re.MULTILINE)

		#line = re.sub(r'\uFFFD', "-", line, flags = re.MULTILINE) #replacement character

		#for replacement of words
		#for key, value in replace_list.my_list.items():
		#for key in keys:

		#line = re.sub(key, value, line, flags=re.MULTILINE)
		my_regex1 = r"([,\"\'\( \/\-\|])" + key + r"([ ,\.!\"।\'\/\-)])"
		my_regex2 = r"([,\"\'\( \/\-\|])" + key + r"$"
		my_regex3 = r"^" + key + r"([ ,\.!\"।\'\/\-)])"
		my_regex4 = r"^" + key + r"$"

		value = all_hash[key]
		#print(line, my_regex1)
		if((re.search(my_regex1, line, re.IGNORECASE|re.UNICODE))):
			#print("regex1",my_regex1,line)
			line = re.sub(my_regex1, r"\1" + value + r"\2", line, flags=re.MULTILINE)


		elif((re.search(my_regex2, line, re.IGNORECASE|re.UNICODE))):
			#print("regex2",my_regex2)
			line = re.sub(my_regex2, r"\1" + value, line, flags=re.MULTILINE)


		elif((re.search(my_regex3, line, re.IGNORECASE|re.UNICODE))):
			#print("regex3",my_regex3,line)
			line = re.sub(my_regex3, value + r"\1", line, flags=re.MULTILINE)


		elif((re.search(my_regex4, line, re.IGNORECASE|re.UNICODE))):
			#print(my_regex4)
			line = re.sub(my_regex4, value, line, flags=re.MULTILINE)

		if(replaceFlag == 'y'):
			line = re.sub(key, value, line)

		#print("before:", line)
		lines[i] = line
		i = i +1
		#print(line)
fpw = open(outfile, "w", encoding='utf-8')
for line in lines:

	#convert multispace to single space
	line = re.sub(r' +', " ", line, flags = re.MULTILINE)
	line = re.sub(r' ।', "।", line, flags = re.MULTILINE)
	#print(line)
	fpw.write(line)