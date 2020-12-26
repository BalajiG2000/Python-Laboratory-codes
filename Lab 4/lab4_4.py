eno=[]
name=[]
eno=input("ENTER ENO NUMBER: ")
name=input("ENTER THE NAME: ")
k=input("ENTER THE ENO TO SEARCH :")
count=0
q=0
for i in eno:
    q+=1
    if i==k:
       count+=1
       break
   
if count==1:
    print "ENO FOUND ;ENO= ",k
    print name[q]
else:
    print "-1"
