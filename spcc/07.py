# Generate Symbol Table
# Enter commands separated by comma
print(' , ,xyz, '.split(','))

code=[
    ' ,START,200, ',
    ' ,MOVER,AREG,DATA',
    ' ,MOVER,BREG,=1',
    ' ,ADD,AREG,BREG',
    ' ,LTORG, , ',
    'DATA,DC,5, ',
    'ST,DS,10, ',
    ' ,ORIGIN,ST+20, ',
    ' ,ADD,CREG,=2',
    ' ,END, , '
    ]
print(*code,sep='\n')

symbolTable=[]

lc = 69     # (˘ ͜ʖ˘) nice
for line in code:
    cmd=line.split(',')

    if cmd[1]=='START':
        lc=int(cmd[2])

    elif cmd[3][0]!='='and cmd[3]!=' 'and "REG"not in cmd[3]:
        if cmd[3] not in [z[0]for z in symbolTable]:
            symbolTable+=[[cmd[3],'-',1]]
            exec("%s=%d"%(cmd[3],69))
        
    elif cmd[0]!=' ':
        if cmd[0] in [z[0]for z in symbolTable]:
            symbolTable[[z[0]for z in symbolTable].index(cmd[0])][1]=lc
            continue
        symbolTable+=[[cmd[0],lc,1]]
        exec("%s=%d"%(cmd[0],lc))
        
    elif cmd[1]=='DS':
        lc+=(int(cmd[2]))
        continue
    
    elif cmd[1]=='ORIGIN':
        exec("%s=%s"%('lc',cmd[2]))
        continue
    lc+=1

print(*symbolTable,sep='\n')
print(len(symbolTable))



        


