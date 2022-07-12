import matplotlib.pyplot as plt
import numpy as np 
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
y=[]
c=0
f=0
s=0.5
for j in range(0,len(n)):
    if j==0:
        for i in np.arange(f,s+0.1,0.1):
            y.append(-1)
        
        f=s
        s+=0.5
        for i in np.arange(f,s,0.1):
            y.append(1)
        c=1
        f=s
        s+=0.5

    elif n[j]==1 and c==0:
        for i in np.arange(f,s,0.1):
            y.append(-1)
        f=s
        s+=0.5
        for i in np.arange(f,s,0.1):
            y.append(1)
        c=1
        f=s
        s+=0.5
    elif n[j]==1 and c==1:
        for i in np.arange(f,s,0.1):
            y.append(1)
        f=s
        s+=0.5
        for i in np.arange(f,s,0.1):
            y.append(-1)
        c=0
        f=s
        s+=0.5
    elif n[j]==0:
        if c==1:
            for i in np.arange(f,s,0.1):
                y.append(-1)
            f=s
            s+=0.5
            
            for i in np.arange(f,s,0.1):
                y.append(1)
            f=s
            s+=0.5
            c=1
        else:
            for i in np.arange(f,s,0.1):
                y.append(1)
            f=s
            s+=0.5
            for i in np.arange(f,s,0.1):
                y.append(-1)
            f=s
            s+=0.5
            c=0

plt.xlim(0,len(y))
plt.ylim(-3,3)
plt.plot(y,drawstyle='steps-pre',linewidth=3)

if n[0]==0:
    plt.plot([0.3,0.3],[-0.99,0.99],color='#1f77b4',linewidth=3)

plt.plot([0,90],[0,0],color='gray')
plt.plot([10,10],[-3,3],'--',color='gray')
plt.plot([20,20],[-3,3],'--',color='gray')
plt.plot([30,30],[-3,3],'--',color='gray')
plt.plot([40,40],[-3,3],'--',color='gray')
plt.plot([50,50],[-3,3],'--',color='gray')
plt.plot([60,60],[-3,3],'--',color='gray')
plt.plot([70,70],[-3,3],'--',color='gray')
plt.plot([80,80],[-3,3],'--',color='gray')
plt.plot([90,90],[-3,3],'--',color='gray')

plt.xlabel(str(n)+'\nTime')
plt.ylabel('Amplitude')
plt.title("Differential Manchester")
plt.show()
