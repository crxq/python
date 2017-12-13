print('.............一起来猜猜..................')


guess = input('猜一猜心里在想着什么数字： ')
num = guess
N = 3
while num != 8:
    N = N - 1
    guess = input('请重新输入数字：')
    if num == 8:
        if N == 2:
            print('你真棒，一次就猜对了')

        else:
            if N == 1:
                print('两次你就猜对了，很厉害')

            else:
                print('好险，但是恭喜你过关了')

    else:
        if num > 8:
            if N == 2:
                print('您输入的数字过大，不过没关系，还有两次机会')

            if N == 1:
                print('您输入的数字过大，不过加油，还有一次机会')

            if N == 0:
                print('对不起，您猜错了')


else:
    if num < 8:
        if N == 2:
            print('您输入的数字过小，不过没关系，还有两次机会')

        if N == 1:
            print('您输入的数字过小，不过加油，还有一次机会')

        if N == 0:
            print('对不起，您猜错了')

print('游戏结束，谢谢参与')

