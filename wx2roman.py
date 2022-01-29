import re
from argparse import ArgumentParser

parser = ArgumentParser(description='#program to find and replace words in the file my making them unique and search in bag and in engine(shell or API) \n\r'+
						"How to Run?\n" +
						"python3 mytransliterate.py -sb=urd-mono-bag.txt -tb=hin-mono-bag.txt -i=urd-mono-sample-text.txt -b=mybag-uniq.csv -o=out.txt -s=urd -t=hin"
						)
parser.add_argument("-i", "--input", dest="inputfile",
					help="provide input file name",required=True)
args = parser.parse_args()

inputfile = args.inputfile

def wx2roman(text):
	text = re.sub(r'lYYq', 'lri', text)
	text = re.sub(r'lYYQ', 'lrI', text)
	text = re.sub(r'lYYa', 'la', text)
	text = re.sub(r'lYY', 'l', text)
	text = re.sub(r'nYa', 'na', text)
	text = re.sub(r'rYa', 'ra', text)
	text = re.sub(r'lYa', 'la', text)
	text = re.sub(r'kZa', 'ka', text)
	text = re.sub(r'KZa', 'kha', text)
	text = re.sub(r'gZa', 'ga', text)
	text = re.sub(r'jZa', 'ja', text)
	text = re.sub(r'PZa', 'pha', text)
	text = re.sub(r'yZa', 'ya', text)
	text = re.sub(r'dZa', '__y7', text)
	text = re.sub(r'DZa', '__y8', text)

	text = re.sub(r'kRq', 'kshri', text)
	text = re.sub(r'wrq', '__p4', text)
	text = re.sub(r'jFq', 'gyri', text)
	text = re.sub(r'Srq', '__p3', text)


	text = re.sub(r'kRQ', 'kshrI', text)
	text = re.sub(r'wrQ', '__p5', text)
	text = re.sub(r'jFQ', 'gyrI', text)
	text = re.sub(r'SrQ', '__p6', text)
	text = re.sub(r'dZq', '__y9', text)
	text = re.sub(r'DZq', '__r1', text)
	text = re.sub(r'dZQ', '__r2', text)
	text = re.sub(r'DZQ', '__r3', text)

	text = re.sub(r'nYq', 'nri', text)
	text = re.sub(r'rYq', 'rri', text)
	text = re.sub(r'lYq', 'lri', text)
	text = re.sub(r'kZq', 'kri', text)
	text = re.sub(r'KZq', 'khri', text)
	text = re.sub(r'gZq', 'gri', text)
	text = re.sub(r'jZq', 'jri', text)

	text = re.sub(r'PZq', 'phri', text)
	text = re.sub(r'yZq', 'yri', text)
	text = re.sub(r'nYQ', 'nrI', text)
	text = re.sub(r'rYQ', 'rrI', text)
	text = re.sub(r'lYQ', 'lrI', text)
	text = re.sub(r'kZQ', 'krI', text)
	text = re.sub(r'KZQ', 'khrI', text)
	text = re.sub(r'gZQ', 'grI', text)
	text = re.sub(r'jZQ', 'jrI', text)
	text = re.sub(r'PZQ', 'phrI', text)
	text = re.sub(r'yZQ', 'yrI', text)

	text = re.sub(r'wr', '__1', text)
	text = re.sub(r'Sr', '__2', text)
	text = re.sub(r'tq', '__3', text)
	text = re.sub(r'Tq', '__4', text)
	text = re.sub(r'dq', '__5', text)
	text = re.sub(r'Dq', '__6', text)
	text = re.sub(r'wq', '__7', text)
	text = re.sub(r'Wq', '__8', text)
	text = re.sub(r'xq', '__9', text)
	text = re.sub(r'Xq', '__p1', text)
	text = re.sub(r'Sq', '__p2', text)
	text = re.sub(r'tQ', '__p7', text)
	text = re.sub(r'TQ', '__p8', text)
	text = re.sub(r'dQ', '__p9', text)
	text = re.sub(r'DQ', '__y1', text)
	text = re.sub(r'wQ', '__y2', text)
	text = re.sub(r'WQ', '__y3', text)
	text = re.sub(r'xQ', '__y4', text)
	text = re.sub(r'XQ', '__y5', text)
	text = re.sub(r'SQ', '__y6', text)
	text = re.sub(r'dZ', '__r4', text)
	text = re.sub(r'DZ', '__r5', text)

	text = re.sub(r'kR', 'ksh', text)
	text = re.sub(r'jF', 'gy', text)
	text = re.sub(r'kq', 'kri', text)
	text = re.sub(r'Kq', 'khri', text)
	text = re.sub(r'gq', 'gri', text)
	text = re.sub(r'Gq', 'ghri', text)
	text = re.sub(r'fq', 'nri', text)
	text = re.sub(r'cq', 'cri', text)
	text = re.sub(r'Cq', 'chri', text)
	text = re.sub(r'jq', 'jri', text)
	text = re.sub(r'Jq', 'jhri', text)
	text = re.sub(r'Fq', 'nri', text)
	text = re.sub(r'Nq', 'nri', text)
	text = re.sub(r'nq', 'nri', text)
	text = re.sub(r'pq', 'pri', text)
	#text = re.sub(r'Pq', 'phri', text)
	text = re.sub(r'Pq', 'fri', text)
	text = re.sub(r'bq', 'bri', text)
	text = re.sub(r'Bq', 'bhri', text)
	text = re.sub(r'mq', 'mri', text)
	text = re.sub(r'yq', 'yri', text)
	text = re.sub(r'rq', 'rri', text)
	text = re.sub(r'lq', 'lri', text)
	text = re.sub(r'vq', 'vri', text)
	text = re.sub(r'Rq', 'shri', text)
	text = re.sub(r'sq', 'sri', text)
	text = re.sub(r'hq', 'hri', text)
	text = re.sub(r'kQ', 'krI', text)
	text = re.sub(r'KQ', 'khrI', text)
	text = re.sub(r'gQ', 'grI', text)
	text = re.sub(r'GQ', 'ghrI', text)
	text = re.sub(r'fQ', 'nrI', text)
	text = re.sub(r'cQ', 'crI', text)

	text = re.sub(r'CQ', 'chrI', text)
	text = re.sub(r'jQ', 'jrI', text)
	text = re.sub(r'JQ', 'jhrI', text)
	text = re.sub(r'FQ', 'nrI', text)
	text = re.sub(r'NQ', 'nrI', text)
	text = re.sub(r'nQ', 'nrI', text)
	text = re.sub(r'pQ', 'prI', text)
	#text = re.sub(r'PQ', 'phrI', text)
	text = re.sub(r'PQ', 'frI', text)
	text = re.sub(r'bQ', 'brI', text)
	text = re.sub(r'BQ', 'bhrI', text)
	text = re.sub(r'mQ', 'mrI', text)
	text = re.sub(r'yQ', 'yrI', text)
	text = re.sub(r'rQ', 'rrI', text)
	text = re.sub(r'lQ', 'lrI', text)
	text = re.sub(r'vQ', 'vrI', text)
	text = re.sub(r'RQ', 'shrI', text)
	text = re.sub(r'sQ', 'srI', text)
	text = re.sub(r'hQ', 'hrI', text)
	text = re.sub(r'eV', 'e', text)
	text = re.sub(r'oV', 'o', text)
	text = re.sub(r'nY', 'n', text)
	text = re.sub(r'rY', 'r', text)
	text = re.sub(r'lY', 'l', text)


	text = re.sub(r'kZ', 'k', text)
	text = re.sub(r'KZ', 'kh', text)
	text = re.sub(r'gZ', 'g', text)
	text = re.sub(r'jZ', 'j', text)
	text = re.sub(r'PZ', 'ph', text)
	text = re.sub(r'yZ', 'y', text)
#---------------------------------------
	text = re.sub(r'aM', 'an', text)
	text = re.sub(r'aH', 'ah', text)
	text = re.sub(r'az', 'an', text)
	text = re.sub(r'Az', 'An', text)
	text = re.sub(r'AM', 'An', text)
	text = re.sub(r'OY', 'o', text)
	text = re.sub(r'EY', 'e', text)
	text = re.sub(r'\u0061', '\u0061', text) # a->a
	text = re.sub(r'\u0041', '\u0041', text) # A->A
	#text = re.sub(r'i', 'i', text)
	#text = re.sub(r'I', 'I', text)
	#text = re.sub(r'u', 'u', text)
	#text = re.sub(r'U', 'U', text)
	#text = re.sub(r'e', 'e', text)
	text = re.sub(r'E', 'ai', text)
	#text = re.sub(r'o', 'o', text)
	text = re.sub(r'O', 'au', text)
	text = re.sub(r'q', 'ri', text)
	text = re.sub(r'Q', 'ri', text)
	text = re.sub(r'L', 'lri', text)
	#text = re.sub(r'k', 'k', text)
	text = re.sub(r'\u004B', 'kh', text)# K->kh
	#text = re.sub(r'g', 'g', text)
	text = re.sub(r'\u0047', 'gh', text) # G->gh
	text = re.sub(r'f', 'n', text)
	text = re.sub(r'c', 'ch', text)
	text = re.sub(r'\u0043', 'chh', text) # C->ch
	#text = re.sub(r'j', 'j', text)
	text = re.sub(r'\u004A', 'jh', text) # J->jh
	text = re.sub(r'F', 'n', text)
	text = re.sub(r'\u0054', 'Th', text) # T->Th
	text = re.sub(r'\u0074', 'T', text) # t->T*******
	text = re.sub(r'\u0044', 'Dh', text) # D->Dh
	text = re.sub(r'\u0064', 'D', text) # d->D********

	text = re.sub(r'\u004E', 'n', text) # N->n
	text = re.sub(r'\u0057', 'th', text) # W->th
	text = re.sub(r'\u0077', 't', text) # w->t

	text = re.sub(r'\u0078', 'd', text) # x->d
	text = re.sub(r'\u0058', 'dh', text) # X->dh
	#text = re.sub(r'n', 'n', text)
	#text = re.sub(r'p', 'p', text)
	#text = re.sub(r'\u0050', 'ph', text) # P->ph
	text = re.sub(r'\u0050', 'ph', text) # P->ph
	#text = re.sub(r'b', 'b', text)
	text = re.sub(r'\u0042', 'bh', text) # B->bh
	#text = re.sub(r'm', 'm', text)
	text = re.sub(r'\u004D', 'n', text) # M->n
	#text = re.sub(r'y', 'y', text)
	#text = re.sub(r'r', 'r', text)
	#text = re.sub(r'l', 'l', text)
	#text = re.sub(r'v', 'v', text)
	#text = re.sub(r's', 's', text)
	text = re.sub(r'\u0053', 'sh', text) # S->sh********
	text = re.sub(r'\u0052', 'sh', text) # R->sh
	#text = re.sub(r'h', 'h', text)
	text = re.sub(r'\u0048', 'h', text) # H -> h
	text = re.sub(r'z', 'n', text) # z->n

#---------------------------
	text = re.sub(r'__1', 'tr', text)
	text = re.sub(r'__2', 'Shr', text)
	text = re.sub(r'__3', 'Tri', text)
	text = re.sub(r'__4', 'Thri', text)
	text = re.sub(r'__5', 'Dri', text)
	text = re.sub(r'__6', 'Dhri', text)
	text = re.sub(r'__7', 'tri', text)
	text = re.sub(r'__8', 'thri', text)
	text = re.sub(r'__9', 'dri', text)
	text = re.sub(r'__p1', 'dhri', text)
	text = re.sub(r'__p2', 'shri', text)
	text = re.sub(r'__p3', 'Shrri', text)
	text = re.sub(r'__p4', 'trri', text)
	text = re.sub(r'__p5', 'trrI', text)
	text = re.sub(r'__p6', 'shrrI', text)
	text = re.sub(r'__p7', 'TrI', text)
	text = re.sub(r'__p8', 'ThrI', text)
	text = re.sub(r'__p9', 'DrI', text)
	text = re.sub(r'__y1', 'DhrI', text)
	text = re.sub(r'__y2', 'trI', text)
	text = re.sub(r'__y3', 'thrI', text)
	text = re.sub(r'__y4', 'drI', text)
	text = re.sub(r'__y5', 'dhrI', text)
	text = re.sub(r'__y6', 'shrI', text)
	text = re.sub(r'__y7', 'Ra', text)
	text = re.sub(r'__y8', 'Rha', text)
	text = re.sub(r'__y9', 'Rri', text)
	text = re.sub(r'__r1', 'Rhri', text)
	text = re.sub(r'__r2', 'RrI', text)
	text = re.sub(r'__r3', 'RhrI', text)
	text = re.sub(r'__r4', 'R', text)
	text = re.sub(r'__r5', 'Rh', text)

        # customization
	text = re.sub(r'I', 'ee', text)
	text = re.sub(r'R', 'd', text)
	text = re.sub(r'T', 't', text)
	text = re.sub(r'D', 'd', text)
	text = re.sub(r'A', 'aa', text)
	text = re.sub(r'U', 'oo', text)

        #remove "a" from word end
	text = re.sub(r'^([\.,\‘\’\(\)]*)([a-zA-Z]+[pfmybsdjgknrthvla])a([\.,\‘\’\(\)\?]*)$', r'\1\2\3', text)

        # normalize words
	text = re.sub(r'^men$', 'mein', text)
	text = re.sub(r'^naheen$', 'nahin', text)

	return text;


#open input file using open file mode
fp1 = open(inputfile, encoding="utf-8") # Open file on read mode
inputs = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

for line in inputs:
    line = wx2roman(line)
    print(line)
#inputs = wx2roman(inputs)
#print(inputs)
