#Edit distance calculation
'''def editDistance(str1, str2, m , n): 
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
str1 = input("Enter first string : ")
str2 = input("Enter second string : ")
print (editDistance(str1, str2, len(str1), len(str2)))'''

#SVD 
'''import numpy
lis=[]
for i in range(0,11):
    l=[]
    for j in range(0,3):
        b=int(input(""))
        l.append(b)
    lis.append(l)
print(lis)
a=numpy.array(lis)
print(a)
u,s,v=numpy.linalg.svd(a,full_matrices=False)
print(u)
print(s)
print(v)'''

#Storing an array to a file and reading from the file
import numpy as np
from math import acos,degrees,sqrt
'''x = np.array([[1, 1, 1], 
              [0, 1, 1],
              [1, 0, 0],
              [0, 1, 0],
              [1, 0, 0],
              [1, 0, 1],
              [1, 1, 1],
              [1, 1, 1],
              [1, 0, 1],
              [0, 2, 0],
              [0, 1, 1]])
'''
'''x=np.array([[1,1],
            [0,1],
            [1,0]])'''
'''np.savetxt("svd.txt", x, delimiter=" ")
y = np.loadtxt("svd.txt",delimiter=" ")

#Performing SVD and storing it in file
u,s,v=np.linalg.svd(y,full_matrices=False)
np.savetxt("u.txt", u, delimiter=" ")
np.savetxt("s.txt", s, delimiter=" ")
np.savetxt("v.txt", v, delimiter=" ")

#Reduce number of dimensions and storing it in file
k=int(input("Enter the number of dimensions : "))
s = np.loadtxt("s.txt",delimiter=" ")
s=s[0:k]
np.savetxt("s_red.txt", s, delimiter=" ")
u = np.loadtxt("u.txt",delimiter=" ")
u = np.transpose(u)
u=u[0:k]
u = np.transpose(u)
np.savetxt("u_red.txt", u, delimiter=" ")
v = np.loadtxt("v.txt",delimiter=" ")
v=v[0:k]
np.savetxt("v_red.txt", v, delimiter=" ")
'''
#Reducing the given query
q = np.array([[0], 
              [0],
              [0],
              [0],
              [0],
              [1],
              [0],
              [0],
              [0],
              [1],
              [1]])
qt=np.transpose(q)
u=np.loadtxt("u_red.txt",delimiter=" ")
s=np.loadtxt("s_red.txt",delimiter=" ")
s1=np.linalg.inv(np.diag(s))
x=np.dot(np.dot(qt,u),s1)
#print(x)
v=np.loadtxt("v_red.txt",delimiter=" ")
v=np.transpose(v)
#print(v)

x=x.tolist()
x=x[0]
v=v.tolist()
angles=[]
a=[]
for i in range(len(v)):
    a=v[i]
    dp=sum([a[j]*x[j] for j in range(len(x))])
    la=sqrt(sum([a[j]**2 for j in range(len(a))]))
    lx=sqrt(sum([x[j]**2 for j in range(len(x))]))
    angle=(dp/(la*lx))
    angle=abs(angle)
    angles.append(angle)
print(angles)
