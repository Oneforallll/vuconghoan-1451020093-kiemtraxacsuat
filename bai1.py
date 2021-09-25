import array as arr
list=[1,1,2,6,8,9,4,5,6,45,34,66,44,37,78]
newlist=[];
for i in list:
    if(i < 30):
        newlist.append(i)
print(newlist)
x=int(input("nhập vào 1 số:"))
a=[];
for i in list:
    if i<x:
        a.append(i)
print(a)