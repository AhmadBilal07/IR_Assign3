from xml.dom import minidom
import Search



mydoc = minidom.parse('topics.xml')
topic = mydoc.getElementsByTagName('topic')
query = mydoc.getElementsByTagName('query')
queryDescription = mydoc.getElementsByTagName('description')



# print(topic.length,query.length,queryDescription.length)
import io
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
I=input("Enter Query\n")


Result=Search.SearchQuery(I)
print("Result",Result)

query=I.split(' ')



word=[]
occurrence=[]
page_no_x=[]
occurrences_in_X=[]





for t, token in enumerate(query):
    token = stemmer.stem(token)
    with io.open("inverted_index.txt", "r", encoding="utf-8") as f:
        for x in f:
            if token in x:
                line=x.split(",")
                if line[0]==token:
                    #print(line)
                    temp = line
                    tem = []
                    tem2 = []
                    tem3 = []
                    if (temp.__len__() > 3):
                        word.append(temp[0])
                        occurrence.append(temp[1])
                        # page_no_x.append(temp[2])
                        j = 2
                        while (j < temp.__len__() - 1):
                            # tem2.append(temp[j])
                            tem.append(temp[j])
                            j = j + 1
                            tem2.append(temp[j])
                            size = int(temp[j], 10)
                            j = j + 1
                            for k in range(0, size):
                                tem3.append(temp[j])
                                j = j + 1

                        page_no_x.append(tem)
                        occurrences_in_X.append(tem2)

N=3495
L=0.9
K=1
b=1.5
S=0
Score=0
import math

print(page_no_x)

for doc in Result:
    print(doc)
    if(doc in page_no_x[0]):
        for i,q in enumerate(query):
            print("Doc Number  ", doc)
            print("Index  No  ", page_no_x[i].index(doc))
            temppppp = page_no_x[i].index(doc)

            print ("lenth of Occurence  ",len(occurrences_in_X) )

            print ("Occurence  ",occurrences_in_X[temppppp] )

            Exp=(K+1)*occurrences_in_X[temppppp]
            print(Exp)
            Score=Score + (math.log((N-len(page_no_x[i])+0.5)/len(page_no_x[i])+0.5))
            print(Score)
'''


            Score= Score + int(math.log2(1/(occurrence[i]+0.5)/(N-occurrence[i]+0.5)))#*(((K+1)*int(occurrences_in_X[page_no_x[0].index(doc)]))/(K*(1-b)+b*L)+int(occurrences_in_X[page_no_x[0].index(doc)])))
            print(Score)


f=open("corpus.qrel", "r")
data= f.read()
data1 = data.split('\n')
topicID = []
docID = []
grade = []
for i in range(0,data1.__len__()):
    temp = data1[i].split(' ')
    if(temp.__len__()>2):
        topicID.append(temp[0])
        docID.append(temp[2])
        grade.append(temp[3])


# for i in range(0,topicID.__len__()):
#     print(topicID[i],docID[i],grade[i])

# print(data1);

#
# for i in range (0,topic.length):
#
#     print(topic[i].attributes['number'].value);
#     print(topic[i].attributes['type'].value);

# for i in range(0, query.length):
#     print(query[i].firstChild.data);

# for i in range(0, queryDescription.length):
    # print(queryDescription[i].firstChild.data);
'''