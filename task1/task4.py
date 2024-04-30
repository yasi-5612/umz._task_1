while 1:
    print('give us current temperature(f or c): ')
    a=input()
    if a=='c' or a=='f':
        break
    else:
        print('invalid action')
if a=='c':
    print('give us temp : ')
    c=input()
    try:
        c=int(c)
    except ValueError:
        c=float(c)
    result= 1.8 * c + 32
    print('temp in fahrenheit is= ',result)
else:
    print('give us temp : ')
    c=input()  
    try:
        c=int(c)
    except ValueError:
        c=float(c)
    result= (c/ 1.8)-32 
    print('temp in fahrenheit is= ',result)