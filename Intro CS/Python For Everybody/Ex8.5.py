FileDir = input('Please Enter The File Directory: ')
File = open(FileDir)
count = 0
for Line in File:
    if Line.startswith('From '):
        Words = Line.split()
        count = count + 1
        print(Words[1])
    else:
        continue
print('There were', count, 'lines in the file with From as the first word')
