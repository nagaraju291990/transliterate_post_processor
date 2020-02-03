#program to find and replace characters/words from machine generated transliterated text
import sys
import re
import os
import replace_list   #custom import file for word replacement

#open file using open file mode

fp1 = open(sys.argv[1]) # Open file on read mode
lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file


for line in lines:

	#character replacement of o to danda
	line = re.sub(r'o', '। ', line, flags = re.MULTILINE)

	#line = re.sub(r'\uFFFD', "-", line, flags = re.MULTILINE) #replacement character

	#for replacement of words
	for key, value in replace_list.my_list.items():

		#line = re.sub(key, value, line, flags=re.MULTILINE)
		my_regex1 = r"([,\"\'\( \/\-\|])" + key + r"([ ,\.!\"।\'\/\-)])"
		my_regex2 = r"([,\"\'\( \/\-\|])" + key + r"$"
		my_regex3 = r"^" + key + r"([ ,\.!\"।\'\/\-)])"
		my_regex4 = r"^" + key + r"$"

		if((re.search(my_regex1, line, re.IGNORECASE|re.UNICODE))):
			#print("regex1",my_regex2)
			line = re.sub(my_regex1, r"\1" + value + r"\2", line, flags=re.MULTILINE)


		elif((re.search(my_regex2, line, re.IGNORECASE|re.UNICODE))):
			#print("regex2",my_regex2)
			line = re.sub(my_regex2, r"\1" + value, line, flags=re.MULTILINE)


		elif((re.search(my_regex3, line, re.IGNORECASE|re.UNICODE))):
			#print("regex3",my_regex2)
			line = re.sub(my_regex3, value + r"\1", line, flags=re.MULTILINE)


		elif((re.search(my_regex4, line, re.IGNORECASE|re.UNICODE))):
			#print(my_regex4)
			line = re.sub(my_regex4, value, line, flags=re.MULTILINE)

		#print("before:", line)
	#convert multispace to single space
	line = re.sub(r' +', " ", line, flags = re.MULTILINE)
	line = re.sub(r' ।', "।", line, flags = re.MULTILINE)
	print(line)
