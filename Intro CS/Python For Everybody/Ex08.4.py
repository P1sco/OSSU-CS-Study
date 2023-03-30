FileDir = input('Please Enter The File Directory: ')
File = open(FileDir)
List = list()
for line in File:
    Words = line.split()
    for Word in Words:
        if Word in List:
            continue
        else:
            List.append(Word)
List.sort()
print(List)
