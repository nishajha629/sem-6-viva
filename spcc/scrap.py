d=69
x='d+15'
exec("%s=%s"%('d',x))
print(d)


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
