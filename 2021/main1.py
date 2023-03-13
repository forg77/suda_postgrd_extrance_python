# 从列表中找出乘积最大的两个数 若有多个结果 返回两数之和最大的 如 L = [1,2,3,4,5] 返回 4,5 ;L[-1,-2,0,1,2] 返回 1,2

if __name__ == '__main__':
    while True:
        L = input().split()  # 1 2 3 4 5 ; -4 -5 1 2 3
        L1 = [int(item) for item in L]
        L1.sort()
        if L1[0] * L1[1] > L1[-1] * L1[-2]:
            print(L1[0], L1[1])  # 5 4
        else:
            print(L1[-1], L1[-2])  # -5 -4
