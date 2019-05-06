from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
I=input("Enter Query\n")

temp=I.split(' ')

arr=[]
finalIndex=[]
fileindex = []


for t, token in enumerate(temp):
    token = stemmer.stem(token)
    print(token)

    import io
    with io.open("inverted_index.txt", "r", encoding="utf-8") as f:
        for x in f:
            if token in x:
                line=x.split(",")
                if line[0]==token:
                    i=2
                    while i < len(line):
                        fileindex.append(line[i])
                        arr.append({"DF":line[1],"TFTD":line[i]})
                        i+=int(line[i+1])+2
   # print(fileindex)
  #  print(len(fileindex))

    if t==0:
        finalIndex=fileindex
    else:
        finalIndex= set(finalIndex).intersection(set(fileindex))



print("Arr--->",arr)
print("Final",finalIndex)





file="docInfo.txt"
with open(file, "r",encoding="utf8") as ins:
    for line in ins:
        line=line.split(',')
        if line[0] in finalIndex:
            print(line[1])
if len(finalIndex)==0:
    print("No Result Found")