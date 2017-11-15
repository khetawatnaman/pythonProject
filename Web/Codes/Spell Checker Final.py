import numpy

#Function to calculate edit distance
def editDistance(str1, str2, m , n): 
    if m==0:
        return n
    if n==0:
        return m
    if str1[m-1]==str2[n-1]:
        return editDistance(str1,str2,m-1,n-1)
    return min(1+editDistance(str1, str2, m, n-1),
               1+editDistance(str1, str2, m-1, n),   
               2+editDistance(str1, str2, m-1, n-1)   
               )

#To find number of matching bigrams
a={}
first=97
for i in range(26):
    second=97
    for j in range(26):
        first_ch=chr(first)
        second_ch=chr(second)
        s=first_ch+second_ch
        second+=1
        a[s]=[]
    first+=1
first=97
for i in range(26):
    first_ch=chr(first)
    s="$"+first_ch
    a[s]=[]
    s=first_ch+"$"
    a[s]=[]
    first+=1
#print(a)
words=['apple','zazz','bazz','bpple','oppo','bajaj','koodo','kooda','akooda','ate','made']
for i in words:
    for j in range(len(i)-1):
        bi=i[j:j+2]
        v=a.get(bi)
        if i not in v:
            v.append(i)
        a.pop(bi)
        a[bi]=v
    bi="$"+i[0]
    v=a.get(bi)
    if i not in v:
        v.append(i)
    a.pop(bi)
    a[bi]=v
    bi=i[len(i)-1]+"$"
    v=a.get(bi)
    if i not in v:
        v.append(i)
    a.pop(bi)
    a[bi]=v
'''for key, value in sorted(a.items()):
    print(key,value)'''

sentence=input("Enter the sentence : ")
word_list=sentence.split(" ")
#print(word_list)

correct_sentence = ""

for iw in word_list:
    #print(iw)
    #print(correct_sentence)
    if iw in words:
        correct_sentence+=iw
        correct_sentence+=" "
        #print(correct_sentence)
    else:
        mb={} #mb is matching bigrams
        for i in range(len(iw)-1):
            bi=iw[i:i+2] # bi is bigram
            v=a.get(bi)
            if len(v)>0:
                for j in v:
                    b=mb.get(j)#if key doen't exist it returns None
                    if b is not None:
                        mb.pop(j)
                        b+=1
                        mb[j]=b
                    else:
                        b=1
                        mb[j]=b
        bi="$"+iw[0]
        v=a.get(bi)
        if len(v)>0:
            for j in v:
                b=mb.get(j)#if key doen't exist it returns None
                if b is not None:
                    mb.pop(j)
                    b+=1
                    mb[j]=b
                else:
                    b=1
                    mb[j]=b
        bi=iw[len(iw)-1]+"$"
        v=a.get(bi)
        if len(v)>0:
            for j in v:
                b=mb.get(j)#if key doen't exist it returns None
                if b is not None:
                    mb.pop(j)
                    b+=1
                    mb[j]=b
                else:
                    b=1
                    mb[j]=b
        #print (mb)
        if len(mb)==0:
            #print("No such word found")
            correct_sentence+=iw
            correct_sentence+=" "
        else:
            mmb=max(mb.values())
            #print(mmb)
            mbl=[]
            for w in mb.keys():
                if mb[w]==mmb:
                    mbl.append(w)
            mbl.sort()
            #print(mbl)
            edmbl=[]
            for i in mbl:
                edmbl.append(editDistance(iw, i, len(iw) ,len(i)))
            #print(edmbl)
            correct_sentence+=mbl[numpy.argmin(edmbl)]
            correct_sentence+=" "

correct_sentence=correct_sentence[0:len(correct_sentence)-1]

print(correct_sentence)
