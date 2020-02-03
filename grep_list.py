#this program will print nukta character containing lines 
import sys
import re

#open input file using open file mode

fp1 = open(sys.argv[1]) # Open file on read mode
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file


for line in lines:
	if(re.search(r'\u093C', line)):
		print(line)
	elif(re.search(r'[\u0958\u0959\u095A\u095B\u095C\u095D\u095E\u095F]', line)):
		print(line)