# 给定一个数列长度大于3 输出 可非连续的 三个从大到小的数 的个数。 例如L=[1,8,5,3,4] 有 8,5,3和8,5,4符合 输出2
# 没有特别的要求 可以n^3解
# 也许有更优的解法 不知道这个n^2方法有没有错误


if __name__ == '__main__':
    while True:
        L = input()  # 1 8 5 3 4
        L = L.split()
        L1 = [int(item) for item in L]
        lenl = len(L1)
        dp = [1] * (lenl + 1)  # 截至i 目前下降序列最大长度
        cnt = 0
        for i in range(lenl):
            for j in range(i + 1, lenl):
                if L[j] < L[i]:
                    dp[j] = max(dp[j], dp[i] + 1)
                    if dp[i] >= 2:
                        cnt += 1  # 可以认为长度至少为3 符合要求

        print(cnt)
