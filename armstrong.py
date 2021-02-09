# WAP for whether the no. is armstrong number

num = int(input())

def Armstrong(num):
    new = num
    sum = 0
    while new > 0:
        dig = new % 10
        sum = sum + dig**3
        new = new // 10
    if num == sum:
        print('{} is an Armstrong Number'.format(num))
    else:
        print('{} is NOT an Armstrong Number'.format(num))
    
    

Armstrong(num)
