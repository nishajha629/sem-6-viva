x=input("Enter String ")
state=0
for i in x:
    if state==0:
        if i=='a':
            state=1
        else:
            state=0     #self loop
    elif state==1:
        if i=='a':
            state=1     #self loop
        else:
            state=2
    else:
        if i=='a':
            state=1
        else:
            state=0

if state==2:
    print("The Input String ends with ab")
else:
    print("The input string does not end with ab")
