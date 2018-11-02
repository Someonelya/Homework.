import random

a=random.randint(1,100)

for i in range(1,10):


    n=input('请输入数字')

    if n.isdigit():

        n=int(n)

        if n==a:

            print('猜对了')

            break

        elif n>a:

            print('大了，再小点')

        else:

            print('小了，再大点')

        

    else:

        print('你输入的不是整数')

    i+=1
