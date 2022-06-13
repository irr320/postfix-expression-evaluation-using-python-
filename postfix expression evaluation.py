# -*- coding: utf-8 -*-
"""
Created on Sun May 15 11:36:28 2022

@author: talk2
"""

st=input("enter the expression")
a=[]
t=-1
count=0
ch=0
for i in range(0,len(st)):
    if st[i].isdigit():
        a.append(st[i])
        t+=1
    elif st[i]=='*':
        ch=int(a[t-1])*int(a[t])
        a.pop()
        a.pop()
        a.append(ch)
        t=t-1
    elif  st[i]=='+':
        ch=int(a[t-1])+int(a[t])
        a.pop()
        a.pop()
        a.append(ch)
        t=t-1
    elif  st[i]=='-':
        ch=int(a[t-1])-int(a[t])
        a.pop()
        a.pop()
        a.append(ch)
        t=t-1
    elif  st[i]=='/':
        ch=int(a[t-1])/int(a[t])
        a.pop()
        a.pop()
        a.append(ch)
        t=t-1
    else:
        count+=1
        break

if count==0:
    print("result is ",a)
    
else:
    print("invalid expression")        
        



































