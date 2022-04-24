# three_address_codes=['t1=a+b','c=t1']
three_address_codes=[input("Enter Address code: "+str(i+1)+": ")for i in range(int(input("Enter no. of codes: ")))]
operators='+-*/'
registers=['-'for _ in range(16)]
last_used_register=-1

for tac in three_address_codes:
    left,right=tac.split('=')
    op1,op2='',''
    operatorExists=False
    for operator in operators:
        if operator not in right:continue
        
        operatorExists=True
        x,y=right.split(operator)
        if x in registers:
            op1=registers.index(x)
        else:
            last_used_register+=1
            op1=last_used_register
            registers[last_used_register]=x
            print(f"MOVF R{last_used_register}, {x}")
        print({'+':f'ADDF R{op1},{y}','-':f'SUBF R{op1},{y}','*':f'MULF R{op1},{y}','/':f'DIVF R{op1},{y}'}[operator])
        
        registers[op1]=left
    if not operatorExists:
        print(f'MOVF {left}, R{registers.index(right)}')




