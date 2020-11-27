import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr)
print(np.__version__)
a=np.array([1,2,3,4,5])
b=np.array([1,2,3,4,5,6,7,8])
c=np.array([[1,2,3,4,5],[6,7,8,9,10]])
d=np.array([[[41,45,112,23],[125,458,47,458]],[[235,146,852,256],[124,412,251,365]]])
arrr=np.array([1,2,3,4],ndmin=5)

#array reshaping
newarr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
barray=newarr.reshape(4,3)
carray=newarr.reshape(2,3,2)
print(barray)
print(carray)

#iterating an array
#goes through each element in the array

g=np.array([[1,2,3],[4,5,7,9]])

for x in g:
    for y in x:
        print(y)
        
#iterating a 3D array
dparr= np.array([[[1,2,5],[4,8,9]], [[7,12,14],[45,88,23]]])



for x in np.nditer(dparr):
    print(x)
#OR
for x in dparr:
    for y in x:
        for  z in y:
            print(z)
            
    



print(arrr)
print(arrr.shape)


#array copying and array viewing
x=b.copy()
y=a.view()
y[0]=77
print(y)
print(a)
x[1]=25
print(x)
print(b)
#array indexing
#print(a[1])
print(b[1])
print(d[0,1,2])
#array slicing
print(b[1:4])
print(b[:4])
print(b[4:])
print(b[-3:-1])
print(b[1:5:2])


#array dimensions
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

