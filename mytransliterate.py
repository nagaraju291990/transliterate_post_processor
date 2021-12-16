#program to find and replace words in the file my making them unique and search in bag and in engine(shell or API)
import sys
import re
import os
import subprocess
#import replace_list   #custom import file for word replacement
from argparse import ArgumentParser

parser = ArgumentParser(description='#program to find and replace words in the file my making them unique and search in bag and in engine(shell or API) \n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=inputfie" + " -r=y|n -b=bagfile.txt -l=urdu"
						)

parser.add_argument("-i", "--input", dest="inputfile",
					help="provide .txt file name",required=True)
parser.add_argument("-r", "--replace", dest="replaceFlag",
					help="replace anywhere in the string",required=False)
parser.add_argument("-b", "--bagfile", dest="listfile",
					help="specify a list file that has tab seperated content", required=True)
parser.add_argument("-s", "--source", dest="srclang",
					help="specify source language;-s=urd|hin|tel", required=True)
parser.add_argument("-t", "--target", dest="tgtlang",
					help="specify target language;-t=urd|hin|tel", required=True)
parser.add_argument("-o", "--outfile", dest="outfile",
					help="specify output file name", required=True)

args = parser.parse_args()

inputfile = args.inputfile
listfile = args.listfile
srclang = args.srclang
tgtlang = args.tgtlang
replaceFlag = args.replaceFlag
outfile = args.outfile

#normalize
def normalize(text):
	text = re.sub(r'\u00A0'," ",text, flags=re.MULTILINE)
	text = re.sub(r'\u2018', "\'", text, flags=re.MULTILINE)
	text = re.sub(r'\u2019', "\'", text, flags=re.MULTILINE)
	text = re.sub(r'\u201C', "\"", text, flags=re.MULTILINE)
	text = re.sub(r'\u201D', "\"", text, flags=re.MULTILINE)
	text = re.sub(r'\u2013', "-", text, flags=re.MULTILINE)
	text = re.sub(r'\u2014', "-", text, flags=re.MULTILINE)
	text = re.sub(r'\ufeff', " ", text, flags=re.MULTILINE)


#tokenize the text- default punctuations and based on language if given in options
def tokenize(text):
	text = re.sub(r'^', ' ', text)
	text = re.sub(r'$', ' ', text)
	text = re.sub(r'([\.,\'\"!\-_\+=\(\):;\?])', r' \1 ', text)
	if(srclang == "urd"):
		text = re.sub(r'([؟،۔])', r' \1 ', text)

	#convert multiple spaces into single space
	text = re.sub(r' +', ' ', text)
	text = re.sub(r'\n', '\n ', text)
	return text

#convert a stream of text into unique list
def get_unique_list(text):
	all_list = text.split(" ")
	u_list = list(set(all_list))
	return u_list

#get machine transliterated text from command
def get_mt_out(ulist):
	fpw1 = open("uwords.txt", "w", encoding='utf-8')
	fpw1.write("\n".join(ulist))
	fpw1.close()
	proc = os.system('/usr/local/bin/indictrans < uwords.txt --s ' + srclang + ' --t ' + tgtlang + ' > tmp.txt')
	fr = open("tmp.txt", "r", encoding='utf-8')
	content = fr.read().split("\n")
	j = 0
	for u in ulist:
		if( u == "\n"):
			continue
		machine_hash[u] = content[j]
		j = j + 1
	fr.close()

#search in bag of words;input=list,output=hash
def transliterate(ulist):
	bag_replaced_hash = {}
	for item in ulist:
		if(item == ""):
			continue
		if(item in bag_hash):
			bag_replaced_hash[item] = bag_hash[item]
		elif(item in machine_hash):
				bag_replaced_hash[item] = machine_hash[item]
		else:
			bag_replaced_hash[item] = item
	return bag_replaced_hash

#replace in original text the words from transliteration
def replaceInText(hash, text):
	keys = hash.keys()
	for key in keys:
		value = hash[key]
		my_regex = r" " + key + r" "
		text = re.sub(my_regex, r' ' + value + r' ', text, flags=re.MULTILINE)
	print(text)
	return text

#detokenize the text after transliteration
def detokenize(text):
	text = re.sub(r' ?\n ?', '\n', text)
	text = re.sub(r' ([\.,\?\)।])', r'\1', text)
	text = re.sub(r'([\'\"!\-_\+=\(:;]।) ', r'\1', text)

	if(tgtlang == "urd"):
		text = re.sub(r' ([؟،۔])', r'\1 ', text)

	if(tgtlang == "hin"):
		text = re.sub(r' ([\?,\.।])', r'\1 ', text)

	text = re.sub(r' +', ' ', text)
	text = re.sub(r'^ ', '', text)
	text = re.sub(r' $', '', text)
	return text

#open input file using open file mode
fp1 = open(inputfile, encoding="utf-8") # Open file on read mode
lines = fp1.read()#.split("\n") # Create a list containing all lines
fp1.close() # Close file

#open list file using open file mode
fp2 = open(listfile, encoding="utf-8") # Open file on read mode
words = fp2.read().split("\n") # Create a list containing all lines
fp2.close() # Close file



machine_hash = {}
bag_hash = {}
#specific for languages
if(srclang == "urd" and tgtlang == "hin"):
	bag_hash["؟"] = "?"
	bag_hash["،"] = ","
	bag_hash["۔"] = "।"

#hash the bag of words
for bag in words:
	if bag == "":
		continue
	word = bag.split("\t")
	bag_hash[word[0]] = word[1]

lines = tokenize(lines)
unique_words = get_unique_list(lines)
#print(unique_words)
get_mt_out(unique_words)
found_hash = transliterate(unique_words)
#print(found_hash)
#print(lines)
lines = replaceInText(found_hash, lines)
#print(lines)
lines = detokenize(lines)

fpw = open(outfile, "w", encoding='utf-8')
fpw.write(lines)
fpw.close()
#print(lines)