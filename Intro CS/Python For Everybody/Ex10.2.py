File = input('Enter File Directory: ')
FileHandle = open(File, 'r')
Dict = dict()
for Line in FileHandle:
    if Line.startswith('From '):
        Line = Line.rstrip()
        Hour = Line[Line.find(":")-2:Line.find(":")]
        Dict[Hour] = Dict.get(Hour, 0) + 1
List = list()
for k, v in Dict.items():
    Tub = (k, v)
    List.append(Tub)
List = sorted(List)
for k, v in List:
    print(k, v)
