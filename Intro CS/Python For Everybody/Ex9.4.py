FileDir = input('Please Enter The File Directory: ')
File = open(FileDir)
EmailDict = dict()
for Line in File:
    if Line.startswith('From '):
        Line = Line.rstrip()
        Words = Line.split()
        # print(Words[1])
        EmailDict[Words[1]] = EmailDict.get(Words[1], 0) + 1
    else:
        continue

EmailID = None
EmailCount = None
for Email, Count in EmailDict.items():
    if EmailCount is None or EmailCount < Count:
        EmailCount = Count
        EmailID = Email
print(EmailID + ' ' + str(EmailCount))
