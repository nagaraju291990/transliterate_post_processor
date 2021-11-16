#this program will print nukta character containing lines 
import sys
import re

#open input file using open file mode

fp1 = open(sys.argv[1]) # Open file on read mode
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

for line in lines:
	if(re.search(r'[\u0642\u062E\u063A\u0630\u0632\u0698\u0638\u0636\u0641\u062D]', line)):	
		print(line)