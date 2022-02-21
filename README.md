
# transliteration post processor
This script will replace an input file with the one provided in list file.
Input file is a machine generated transliterated(or could be any general) file

## How to run?

### Post Processor
    python3 post_processor.py -i=inputfile.txt  -l=list.txt -r=y

### Transliterate -- Mytransliterate.py
	python3 mytransliterate.py -sb=urd-mono-bag.txt -tb=hin-mono-bag.txt -i=urd-mono-sample-text.txt -b=mybag-uniq.csv -o=out.txt -s=urd -t=hin

### list.txt
```bash
It is a tab seperated file with column1 containing what to search for and 
column2 containing what to replace with
```

## nukta fixer
This program will generate nuktas wherver necessary
```bash
python3 nukta.py inputfile
```
## grep list

This script will extract nukta characters from input file

```bash
python3 grep_list.py inputfile
```

## extract hyphenated words from translated file
```
python3 hyphenated_words.py -i=input.xlsx extract hyphenated words -b=bag.txt
```
