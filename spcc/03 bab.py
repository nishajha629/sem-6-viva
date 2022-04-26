x=input("Enter String ")
state=0
for i in x:
    if state==0:
        if i=='a':
            state=0     #self loop
        else:
            state=1
    elif state==1:
        if i=='a':
            state=2
        else:
            state=1     #self loop
    elif state==2:
        if i=='a':
            state=0
        else:
            state=3
    

print('The String contains bab'if state==3 else 'The String does not contain bab')
