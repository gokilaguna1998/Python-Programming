try :
    value=0
    val=input('Enter the number : ')
    st=str(val)
    le=len(st)
    for i in range(0,le,1) :
        value += int(st[i])**le
    if value==int(val) :
        print("yes")
    else :
        print('no')
except :
        print ("something is error")
