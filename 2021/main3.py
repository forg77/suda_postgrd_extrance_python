# 给出n 求出1-n中二进制表示 1数量大于0数量的数
# n=15 返回 [1,3,5,6,7,11,13,14,15]
# 按照要求做就行


def check_10(n):
    cnt0 = 0
    cnt1 = 0
    while n != 0:
        if n % 2 == 0:
            cnt0 += 1
        else:
            cnt1 += 1
        n //= 2
    return cnt1 > cnt0

if __name__ == '__main__':
    ans = []
    n = int(input())
    for i in range(n+1):
        if check_10(i):
            ans.append(i)
    print(ans)
