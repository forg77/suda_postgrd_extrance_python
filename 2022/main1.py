# 求一个数字由几个素数相乘得到 10=2*5 输出2 18=2*3*3 输出3
# 因为没指定范围 就边判断边计算
from math import sqrt


def prime(n):
    t = int(sqrt(n))
    fail = False
    for i in range(2, t + 1):
        if n % i == 0:
            fail = True
            break
    return not fail


def solve(n):
    t = int(sqrt(n))
    cur = 2
    cnt = 1
    while n != 1 and cur <= t:
        if prime(cur):
            while (n % cur == 0):
                n /= cur
                cnt += 1
        cur += 1
        if prime(n):
            break
    if n == 1:
        cnt -= 1
    return cnt


if __name__ == '__main__':
    while True:
        n = int(input())
        ans = solve(n)
        print(ans)
