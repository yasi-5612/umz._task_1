def thief():
    a3="true"
    a1="true"
    c1='false'
    c3='false'
    d2='true'
    a2="true" 
    b1='true'  
    b3=''
    b2=''
    c2=''
    d1=''
    d3=''
    false_count=2
    true_count=5
    while false_count<6:
        if a2=='true':
            b3='false'
            false_count+=1
            if b3=='false':
                d3='false'
                false_count+=1
                b2='true'
                true_count+=1
                if true_count==6:
                    c2='false'
                    d1='false'
                    false_count+=2
                    

            else:
                break
            
        else :
            a2='false' 
            false_count+=1
            break
    if (true_count==6 and false_count==6):
        print('the thief is B')

thief()