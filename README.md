
# transliteration post processor
This script will replace an input file with the one provided in list file.
Input file is a machine generated transliterated(or could be any general) file

## How to run?

    python3 post_processor.py -i=inputfile.txt  -l=list.txt -r=y

### list.txt
```bash
It is a tab seperated file with column1 containing what to search for and 
column2 containing what to replace with
```

## grep list

This script will extract nukta characters from input file

```bash
python3 grep_list.py inputfile
```
