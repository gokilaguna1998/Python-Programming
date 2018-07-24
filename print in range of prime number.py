for msg in range(1,10):
    for i in range(2,msg):
        if (msg%i==0):
            break
        else:
            print(msg)
            break
