#  求10-1000间满足以下两条件的数 存储在result.txt中
#  1 素数 2 反数也是素数 123 与 321
from math import sqrt
FILE_PATH = 'result.txt'


def check(temp):
    False1 = False
    False2 = False
    t = int(sqrt(temp))
    for i in range(2,t+1):
        if temp % i == 0:
            False1 = True
            break
    tempr = "".join(reversed(str(temp)))
    tempr = int(tempr)
    t = int(sqrt(tempr))
    for i in range(2,t+1):
        if tempr % i == 0:
            False2 = True
            break
    return (not False1) and (not False2)
if __name__ == '__main__':
    lower = 10
    upper = 1000
    ans = []
    for i in range(lower,upper+1):
        if check(i):
            ans.append(i)
    fp = open(FILE_PATH,'w')
    fp.write(str(ans))
    fp.close()
