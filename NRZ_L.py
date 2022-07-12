import numpy as np 
import matplotlib.pyplot as plt
import math

print('Enter your ids last 3 digit :', end=' ' )
Student_Id = int(input())
n=[]
while Student_Id!=0:
    n.append(Student_Id % 2)
    Student_Id =math.floor(Student_Id/ 2)

for i in range(0,8-len(n)):
    n.append(0)

n.reverse()
print(n)

nn=[]

for k in range(0,len(n)):
    if n[k]==1:
        nn.insert(k,3)
    else:
        nn.insert(k,-3)
t=[]
y=[]
for  k in np.arange(0, len(n), 0.01):
    t.append(k)
i=1
a=0.5
k=0
for j in range(0,len(t)):
    if t[j]<i:
        y.insert(j,nn[k])
    else:
        i=i+1
        k+=1
        y.insert(j,nn[k])
        
plt.xlim(0,len(n))
plt.ylim(-10,10)
plt.xlabel(str(n)+'\nTime')
plt.ylabel('Amplitude')
plt.title('Polar-NRZ-L')
plt.plot([0,len(n)],[0,0],color='gray')
plt.plot(t,y,linewidth=3)

for i in range(1,len(n)+1):
    plt.plot([i,i],[-10,10],'--',color='gray')


plt.show()