import re
# File = input('Please Enter The File Directory')
FileHandler = open('d:/Numbers.txt')
NumbersList = []
for Line in FileHandler:
    Line = Line.rstrip()
    Numbers = re.findall('[0-9]+', Line)
    if len(Numbers) != 0:
        Numbers = [int(i)for i in Numbers]
        NumbersList.extend(Numbers)
Summary = sum(NumbersList)
print(Summary)
