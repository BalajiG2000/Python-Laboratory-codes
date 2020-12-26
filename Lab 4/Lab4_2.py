l=[]
l=input("Enter the elements: ")
count=0
i=0
while i<len(l)-1:
        if l[i]==l[i+1]:
            count+=1
        i+=1    
print count
