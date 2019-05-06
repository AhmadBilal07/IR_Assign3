from xml.dom import minidom

mydoc = minidom.parse('topics.xml')
topic = mydoc.getElementsByTagName('topic')
query = mydoc.getElementsByTagName('query')
queryDescription = mydoc.getElementsByTagName('description')

# print(topic.length,query.length,queryDescription.length)

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
#     print(queryDescription[i].firstChild.data);

fs=open("inverted_index.txt", encoding="utf-8")
fi= fs.read()
fi1 = fi.split('\n')
word=[]
occurrence=[]
page_no_x=[]
occurrences_in_X=[]
word_no=[]
for i in range(0,fi1.__len__()):
    temp= fi1[i].split(',')
    tem = []
    tem2 = []
    tem3 = []
    if(temp.__len__()>3):
        word.append(temp[0])
        occurrence.append(temp[1])
        # page_no_x.append(temp[2])
        j=2
        while(j<temp.__len__()-1):
           # tem2.append(temp[j])
            tem.append(temp[j])
            j=j+1
            tem2.append(temp[j])
            size= int(temp[j],10)
            j = j + 1
            for k in range(0,size):
                tem3.append(temp[j])
                j=j+1
                # print(j)
            # print(j,j+1)


        page_no_x.append(tem)
        occurrences_in_X.append(tem2)
        word_no.append(tem3)

for i in range(0,10):
    print(word[i],occurrence[i],page_no_x[i],occurrences_in_X[i],word_no[i])


