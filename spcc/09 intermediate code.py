from ast import literal_eval


imperative=['STOP','ADD','SUB','MULT','MOVER','MOVEM','COMP','BC','DIV','READ','PRINT']
declarative=['yourmom','DS','DC']
assembler=['yourmom ','START','END','ORIGIN','EQU','LTORG']
registers=['yourmom','AREG','BREG','CREG','DREG','EREG','FREG']


code=[
    ' ,START,200, ',
    ' ,MOVER,BREG,=1',
    ' ,MOVER,AREG,DATA',
    'DATA,DC,5, ',
    ' ,LTORG, , ',
    ' ,ORIGIN,400, ',
    ' ,ADD,CREG,=2',
    ' ,END, , '
    ]
literal_table=[['=1',203],['=2',401]]
symbol_table=[['DATA',202]]
intermediate_code=[]
for cmd in code:
    line=[]
    cmd=cmd.split(',')
    for word in cmd:
        if word in imperative:
            line+=[('IS',imperative.index(word))]
        if word in declarative:
            line+=[('DL',declarative.index(word))]
        if word in assembler:
            line+=[('IS',assembler.index(word))]
        if word in registers:
            line+=[('RG',registers.index(word))]
        if word in [x[0]for x in symbol_table]:
            line+=[('S',[x[0]for x in symbol_table].index(word))]
        if word in [x[0]for x in literal_table]:
            line+=[('L',[x[0]for x in literal_table].index(word))]



