identifier=input("Enter Identifier ")
state=0
if identifier[0]=='_' or identifier[0].isalpha():
    state=1
else:
    state=2
if state==1:
    print("The Identifier is valid")
else:
    print("The Identifier is Invalid")