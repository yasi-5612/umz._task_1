while 1:
    while 1:
        print('please give us operation :\n(sum,divide,difference,multiple)')
        a=input()
        if a=='sum' or a=='divide' or a=='difference' or a=='multiple':
            break
        else:
            print('invalid') 
    print("please give us numbers")
    b=input()
    c=input()
    try:
       b=int(b)
    except ValueError:
           b=float(b)
    try:
       c=int(c)
    except ValueError:
           c=float(c)
    if a=='sum':
        result = b+c
        print('the answre is : ',result)
    elif a=='difference':
        result = b-c
        print('the answre is : ',result)
    elif a=='multiple':
        result = b*c
        print('the answre is : ',result)
    elif a=='divide':
        if c==0 :
            print('cant divide by zero')
        else:
            result = b/c
            print('the answre is : ',result)