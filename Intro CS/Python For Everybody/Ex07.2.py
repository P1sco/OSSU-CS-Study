FileName = input('Please Enter The File Directory: ')
FileHandle = open(FileName)
Count = 0
Summary = 0
for Line in FileHandle:
    if not Line.startswith('X-DSPAM-Confidence:'):
        continue
    StartingPos = Line.find(':')
    EndingPos = len(Line)
    Confidence = Line[StartingPos+1:EndingPos]
    Count = Count + 1
    Summary = Summary + float(Confidence)
    Average = Summary / Count
print('Average spam confidence: ' + str(Average))
