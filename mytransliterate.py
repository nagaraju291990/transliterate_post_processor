#program to find and replace words in the file my making them unique and search in bag and in engine(shell or API)
import sys
import re
import os
import subprocess
#import replace_list   #custom import file for word replacement
from argparse import ArgumentParser
import logger as log

parser = ArgumentParser(description='#program to find and replace words in the file my making them unique and search in bag and in engine(shell or API) \n\r'+
						"How to Run?\n" +
						"python3 mytransliterate.py -sb=urd-mono-bag.txt -tb=hin-mono-bag.txt -i=urd-mono-sample-text.txt -b=mybag-uniq.csv -o=out.txt -s=urd -t=hin"
						)

parser.add_argument("-i", "--input", dest="inputfile",
					help="provide .txt file name",required=True)
#parser.add_argument("-r", "--replace", dest="replaceFlag",
#					help="replace anywhere in the string",required=False)
parser.add_argument("-bb", "--bagfile", dest="listfile",
					help="specify a list file that has tab seperated content", required=True)
parser.add_argument("-s", "--source", dest="srclang",
					help="specify source language;-s=urd|hin|tel", required=True)
parser.add_argument("-sb", "--preprocessbag", dest="srcbag",
					help="specify pre processor bag;-sb=pre.bag", required=True)
parser.add_argument("-t", "--target", dest="tgtlang",
					help="specify target language;-t=urd|hin|tel", required=True)
parser.add_argument("-tb", "--postprocessbag", dest="tgtbag",
					help="specify post processor bag;-tb=post.bag", required=True)
parser.add_argument("-o", "--outfile", dest="outfile",
					help="specify output file name", required=True)

log.logging.info("Parsing command line arguments")

args = parser.parse_args()

inputfile = args.inputfile
listfile = args.listfile
srclang = args.srclang
tgtlang = args.tgtlang
srcbag = args.srcbag
tgtbag = args.tgtbag
#replaceFlag = args.replaceFlag
outfile = args.outfile

log.logging.info("Received following arguments: inputfile=%s, listfile=%s, source language=%s, target language=%s, srcbag=%s, tgtbag=%s, output file=%s" %(inputfile, listfile, srclang, tgtlang, srcbag, tgtbag, outfile))

#normalize
def normalize(text):
	text = re.sub(r'\’\’', "\"", text)	#convert two consecutive 2019 single quotes into double quotes
	text = re.sub(r'\‘\‘', "\"", text)	#convert two consecutive 2018 single quote into double quotes
	text = re.sub(r'\u00A0', " ", text, flags=re.MULTILINE)
	text = re.sub(r'\u2018', "\'", text, flags=re.MULTILINE)
	text = re.sub(r'\u2019', "\'", text, flags=re.MULTILINE)
	text = re.sub(r'\u201C', "\"", text, flags=re.MULTILINE)
	text = re.sub(r'\u201D', "\"", text, flags=re.MULTILINE)
	text = re.sub(r'\u2013', "-", text, flags=re.MULTILINE)
	#text = re.sub(r'\u2014', "-", text, flags=re.MULTILINE)
	text = re.sub(r'\ufeff', " ", text, flags=re.MULTILINE)
	text = re.sub(r':۔', ":-", text, flags=re.MULTILINE)
	return text

#pre process
def pre_process(text, hash):
	log.logging.info("In Pre Process Function, text=%s" %(text))
	#Rules
	keys = hash.keys()
	log.logging.info("Pre Process Function before subsitution from pre process bag, text=%s" %(text))
	for key in keys:
		value = hash[key]
		#my_regex = r" " + re.escape(key) + r" "#r"(?= )"
		my_regex = r"(^|[,\"\'\( \/\|\n])" + key + r"([ ,\.!\"।\'\/\;\:)\n]|$)"
		text = re.sub(my_regex, r"\1" + value + r"\2" , text, flags=re.UNICODE)
	log.logging.info("Pre Process Function after subsitution from pre process bag, text=%s" %(text))
	return text

#tokenize the text- default punctuations and based on language if given in options
def tokenize(text):
	text = re.sub(r'^', ' ', text)
	text = re.sub(r'$', ' ', text)
	text = re.sub(r'([\.]{3,})', '__ELLIP3__ ', text)
	text = re.sub(r'([\.]{2,2})', '__ELLIP2__ ', text)
	text = re.sub(r'([۔]{3,})', ' __ARABIC3__ ', text)
	text = re.sub(r'([۔]{2,2})', ' __ARABIC2__ ', text)
	text = re.sub(r'([\.,\'\"!\-_\+=\(\):;\?—])', r'  \1  ', text)
	if(srclang == "urd"):
		text = re.sub(r'([؟،۔])', r' \1 ', text)

	#convert multiple spaces into single space
	text = re.sub(r' +', ' ', text)
	text = re.sub(r'\n', ' \n ', text)
	return text

#convert a stream of text into unique list
def get_unique_list(text):
	text = text.replace("\n", "")
	all_list = text.split(" ")
	u_list = list(set(all_list))
	u_list = [ul  for ul in u_list  if not re.match(r'^[\u0900-\u09FF]+$', ul)]
	#print(u_list)
	return u_list

#get machine transliterated text from command
def get_mt_out(ulist):
	if(os.system('/usr/local/bin/indictrans --version > /dev/null 2>&1') != 0):
		print ('indictrans does not exist in your machine, so skipping this section.')
		return

	fpw1 = open("uwords.txt", "w", encoding='utf-8')
	fpw1.write("\n".join(ulist))
	fpw1.close()
	proc = os.system('/usr/local/bin/indictrans < uwords.txt --s ' + srclang + ' --t ' + tgtlang + ' > tmp.txt')
	fr = open("tmp.txt", "r", encoding='utf-8')
	content = fr.read().split("\n")
	j = 0
	for u in ulist:
		#if( u == "\n"):
			#continue
		machine_hash[u] = content[j]
		j = j + 1
	#print(content)
	fr.close()

#search in bag of words;input=list,output=hash
def transliterate(ulist):
	bag_replaced_hash = {}
	for item in ulist:
		if(item == ""):
			continue
		if(item in bag_hash):
			log.logging.info("Found word in user bag;word=|%s|,target=|%s|" %(item, bag_hash[item]))
			bag_replaced_hash[item] = bag_hash[item]
		elif(item in machine_hash):
			log.logging.info("Found word in machine transliteration;word=|%s|,target=|%s|" %(item, machine_hash[item]))
			bag_replaced_hash[item] = machine_hash[item]
		else:
			log.logging.info("Word not found in either user bag or machine transliteration;word=|%s|" %(item))
			bag_replaced_hash[item] = item
	return bag_replaced_hash

#replace in original text the words from transliteration
def replaceInText(hash, text):
	keys = hash.keys()
	log.logging.info("replaceInText Function before subsitution, text=%s" %(text))
	for key in keys:
		value = hash[key]
		my_regex = r" " + re.escape(key) + r" "#r"(?= )"
		text = re.sub(my_regex, r" " + value + " " , text, flags=re.UNICODE)
	log.logging.info("replaceInText Function after subsitution, text=%s" %(text))
	return text

#detokenize the text after transliteration
def detokenize(text):

	text = re.sub(r' ([\.,\?\)।])', r'\1', text)
	text = re.sub(r' ([!\-\_\+=:;।—]) ?', r'\1', text)
	text = re.sub(r'__ ?ELLIP3__', '...', text)
	text = re.sub(r'__ ?ELLIP2__', '..', text)
	text = re.sub(r'__ ?ARABIC3__', '...', text)
	text = re.sub(r'__ ?ARABIC2__', '..', text)
	text = re.sub(r'\( ', '(', text)
	text = re.sub(r'([\'\"]) ', r'\1', text)
	text = re.sub(r'( +)?\n( +)?', '\n', text)

	if(tgtlang == "urd"):
		text = re.sub(r' ([؟،۔])', r'\1 ', text)

	if(tgtlang == "hin"):
		text = re.sub(r'\b([\?,\.।])\b', r'\1 ', text)

	# case-1
	text = re.sub(r'([\u0900-\u09FF]+) ([\u0600-\u06FF]+)', r'\1-\1', text)
	#case2,3
	text = re.sub(r'([!]{1,})([\'\"])?', r'\1\2 ', text)
	#case-4
	text = re.sub(r':', ': ', text)
	#case-5
	text = re.sub(r'([0-9]+)([\.]) ([0-9]+)', r'\1\2\3', text)
	#case-6
	text = re.sub(r'([0-9]+)([\.])([0-9]+)([।])', r'\1\2\3.', text)
	#case-7,8
	text = re.sub(r'(\n[\u0900-\u09FF]+) ([\u0900-\u09FF]+)([।])', r'\1 \2-', text)
	text = re.sub(r'(\n[\u0900-\u09FF]+)([।])', r'\1-', text)
	#case-9,10
	text = re.sub(r'([।\?])([\'\"])', r'\1\2 ', text)
	# case-11,12
	text = re.sub(r'([।\?]) ([\'\"])', r'\1\2 ', text)
	# case-13,14
	text = re.sub(r'( )([\'\"])([,!])', r'\2\3 ', text)
	# case-15
	text = re.sub(r'([,])([\'\"])([\u0900-\u09FF]+)', r'\1 \2\3 ', text)
	# case-16
	text = re.sub(r'([\u0900-\u09FF]+)([\'\"])([\u0900-\u09FF]+)', r'\1\2 \3 ', text)
	# case-17
	text = re.sub(r'([\)])([\'\"])([\u0900-\u09FF]+)', r'\1 \2\3 ', text)


	text = re.sub(r' +', ' ', text)
	text = re.sub(r'^ ', '', text)
	text = re.sub(r' $', '', text)
	text = re.sub(r' \"(\u0964)', r'"\1', text)
	return text

# Post process function
def post_process(text, hash):
	log.logging.info("In Post Process Function, text=%s" %(text))
	text = re.sub(r'(\b[\u0900-\u09FF]+\b) व (\b[\u0900-\u09FF]+\b)', r'\1-व-\2', text)
	#text = re.sub(r'(\b[\u0900-\u09FF]+\b) ए (\b[\u0900-\u09FF]+\b)', r'\1-ए-\2', text)
	#text = re.sub(r'(\b[\u0900-\u09FF]+\b) अ (\b[\u0900-\u09FF]+\b)', r'\1-अ-\2', text)
        # ge,ga, gi - गे,गा,गी
	text = re.sub(r'([\u0900-\u09FF]+) (\u0917\u0947|\u0917\u093E|\u0917\u0940)', r'\1\2', text)
	text = re.sub(r'( [\u0900-\u09FF]+)(\u0939\u0948[\u0902]*\u0964)', r'\1 \2', text)
	keys = hash.keys()
	log.logging.info("Post Process Function before subsitution from post process bag, text=%s" %(text))
	for key in keys:
		value = hash[key]
		#my_regex = r" " + re.escape(key) + r" "#r"(?= )"
		my_regex = r"(^|[,\"\'\( \/\|\n])" + key + r"([ ,\.!\"।\'\/\;\:)\n]|$)"
		log.logging.info("Current word is;key=|%s|,target=|%s|" %(key, hash[key]))
		text = re.sub(my_regex, r"\1" + value + r"\2" , text, flags=re.UNICODE)
	log.logging.info("Post Process Function after subsitution from post process bag, text=%s" %(text))
	return text

#open input file using open file mode
fp1 = open(inputfile, encoding="utf-8") # Open file on read mode
lines = fp1.read().strip()#.split("\n") # Create a list containing all lines
fp1.close() # Close file

#open list file using open file mode
fp2 = open(listfile, encoding="utf-8") # Open file on read mode
words = fp2.read().split("\n") # Create a list containing all lines
fp2.close() # Close file

#open list file using open file mode
fp3 = open(srcbag, encoding="utf-8") # Open file on read mode
srcbag_words = fp3.read().split("\n") # Create a list containing all lines
fp3.close() # Close file

#open list file using open file mode
fp4 = open(tgtbag, encoding="utf-8") # Open file on read mode
tgtbag_words = fp4.read().split("\n") # Create a list containing all lines
fp4.close() # Close file

machine_hash = {}
bag_hash = {}

six_word_hash = {}
five_word_hash = {}
four_word_hash = {}
three_word_hash = {}
two_word_hash = {}
word_hash = {}

src_bag_hash = {}
tgt_bag_hash = {}
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

#hash the bag of words
for src in srcbag_words:
	if src == "":
		continue
	word = src.split("\t")
	#src_bag_hash[word[0]] = word[1]
	if(len(re.findall(" ", word[0])) == 5 ):
		six_word_hash[word[0]] = word[1]
	elif(len(re.findall(" ", word[0])) == 4 ):
		five_word_hash[word[0]] = word[1]
	elif(len(re.findall(" ", word[0])) == 3 ):
		four_word_hash[word[0]] = word[1]
	elif(len(re.findall(" ", word[0])) == 2 ):
		three_word_hash[word[0]] = word[1]
	elif(len(re.findall(" ", word[0])) == 1 ):
		two_word_hash[word[0]] = word[1]
	else:
		word_hash[word[0]] = word[1]

for d in (six_word_hash, five_word_hash, four_word_hash, three_word_hash, two_word_hash, word_hash):
	src_bag_hash.update(d)

six_word_hash = {}
five_word_hash = {}
four_word_hash = {}
three_word_hash = {}
two_word_hash = {}
word_hash = {}

#hash the bag of words
for tgt in tgtbag_words:
	if tgt == "":
		continue
	word = tgt.split("\t")
	#tgt_bag_hash[word[0]] = word[1]
	if(len(re.findall(" ", word[0])) == 5 ):
		six_word_hash[word[0]] = word[1]
	elif(len(re.findall(" ", word[0])) == 4 ):
		five_word_hash[word[0]] = word[1]
	elif(len(re.findall(" ", word[0])) == 3 ):
		four_word_hash[word[0]] = word[1]
	elif(len(re.findall(" ", word[0])) == 2 ):
		three_word_hash[word[0]] = word[1]
	elif(len(re.findall(" ", word[0])) == 1 ):
		two_word_hash[word[0]] = word[1]
	else:
		word_hash[word[0]] = word[1]

for d in (six_word_hash, five_word_hash, four_word_hash, three_word_hash, two_word_hash, word_hash):
	tgt_bag_hash.update(d)
#print(src_bag_hash)
#print(tgt_bag_hash)
log.logging.info("Going into normalize function: text=|%s|" %(lines))

lines = normalize(lines)
log.logging.info("After normalize function: text=|%s|" %(lines))
log.logging.info("Going into pre process function")

lines = pre_process(lines, src_bag_hash)
log.logging.info("After pre process function text=|%s|" %(lines))
log.logging.info("Going into tokenize function")

lines = tokenize(lines)
log.logging.info("After tokenize function: text=|%s|" %(lines))
log.logging.info("Going into get_unique_list function")

unique_words = get_unique_list(lines)
log.logging.info("After get_unique_list function: unique_list=|%s|" %("____".join(unique_words)))
log.logging.info("Going into get_mt_out function")

get_mt_out(unique_words)
log.logging.info("After get_mt_out function: generated uwords.txt and temp.txt files and saved each unique_word mt output in hash=%s" %(machine_hash))
log.logging.info("Going into transliterate function")

found_hash = transliterate(unique_words)
log.logging.info("After transliterate function a hash is generated that contains key as each word from input and value as output from either the bag or mtoutput; hash=%s" %(found_hash))
log.logging.info("Going into replaceInText function: text=|%s|" %(lines))
#print(found_hash)

lines = replaceInText(found_hash, lines)
log.logging.info("After replaceInText function: text=|%s|" %(lines))
log.logging.info("Going into detokenize function")

lines = detokenize(lines)
log.logging.info("After detokenize function text=|%s|" %(lines))
log.logging.info("Going into post_process function")

lines = post_process(lines, tgt_bag_hash)
log.logging.info("After post_process function text=|%s|" %(lines))
log.logging.info("Writing output to outfile=|%s|" %(outfile))

fpw = open(outfile, "w", encoding='utf-8')
fpw.write(lines)
fpw.close()
