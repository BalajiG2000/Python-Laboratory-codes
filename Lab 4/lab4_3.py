l=[]
l=input()
n=len(l)
least=l[0]
highest=l[n-1]
for i in l:
    print i,
    if i<least:
        least=i
        
    if i>highest:
        highest=i
print " Least= ",least,"Highest = ",highest
for i in range(len(l)):
    if highest==l[i]:
        k=i
    if least==l[i]:
        q=i
l[k],l[q]=l[q],l[k]
for i in l:
    print i,

    
