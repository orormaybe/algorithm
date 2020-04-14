import numpy as np
x=np.array([[3,3],[4,3],[1,1]])
y=np.array([1,1,-1])
b=0
a=np.array([0,0,0])
gram=np.zeros([3,3])
for i in range(3):
    for j in range(3):
        gram[i][j]=x[i][0]*x[j][0]+x[i][1]*x[j][1]
k=0
sum=0
while k<3:
    sum=y[k]*((a[0]*y[0]*gram[0][k]+a[1]*y[1]*gram[1][k]+a[2]*y[2]*gram[2][k])+b)
    if(sum<=0):
        a[k]+=1
        b+=y[k]
        k=0
    else:
        k+=1
print(b)
print(a[0]*y[0]*x[0]+a[1]*y[1]*x[1]+a[2]*y[2]*x[2])
