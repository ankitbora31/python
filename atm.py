try:
    a, b = input().split()
    a = int(a)
    b = float(b)
    
    if a%5==0:
        if a<b:
            balance = b - a - 0.5
            print('{0:.2f}'.format(balance))
        else:
            print('{0:.2f}'.format(b))
    else:
        print('{0:.2f}'.format(b))
except:
    pass
