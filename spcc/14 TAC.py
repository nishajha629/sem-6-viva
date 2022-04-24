input_str=input("Enter the eq: ")
init_counter,precedence=1,'*/+-'
for i in precedence:
    while input_str.find(i)!=-1:
        loc=input_str.find(i)
        print(f'{init_counter} = {input_str[loc-1:loc+2]}')
        input_str=input_str[:loc-1]+f'{init_counter}'+input_str[loc+2:]
        init_counter+=1