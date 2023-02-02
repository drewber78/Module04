# Lab 4-1 Working with Tuples
'''
1. Create a script that uses a tuple to hold the following data:

	1  "Bob Smith"  "BSmith@Hotmail.com"

2. Add code to print out the row of the data
'''

tab = '\t'
tplData1 = (1, 'Bob Smith', 'BSmith@hotmail.com')
tplHeader = ('ID', 'Name', 'Email')
tpltable = (tplHeader, tplData1)

#item = 0
for item in tpltable:
    print(item[0], item[1], item[2], sep='\t')#, tplHeader[1], tplHeader[2])
    #item += 1
#print(tplData1)
