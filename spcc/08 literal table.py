
code=[
    ' ,START,200, ',
    ' ,MOVER,BREG,=1',
    ' ,LTORG, , ',
    ' ,ADD,CREG,=2',
    ' ,END, , '
    ]

lc = 69     # (˘ ͜ʖ˘) nice
literal_table=[['Literal', 'Add']]
for cmd in code:
    cmd=cmd.split(',')
    if cmd[1]=='START':
        lc=int(cmd[2])
        continue
    elif cmd[3][0]=='=':
        if cmd[3]not in [z[0]for z in literal_table]:
            literal_table+=[[cmd[3],'-']]
    
    elif cmd[1]=='LTORG':
        for i in range(len(literal_table)):
            if literal_table[i][1]=='-':
                literal_table[i][1]=lc
                lc+=1
        continue
    
    elif cmd[1]=='END':
        for i in range(len(literal_table)):
            if literal_table[i][1]=='-':
                literal_table[i][1]=lc
                lc+=1
        continue
    lc+=1

print("The Literal Table is")
for x in literal_table:
    print(*x,sep=' ')
        

