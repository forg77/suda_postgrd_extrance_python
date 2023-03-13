# 编写一个函数check(L)判断列表L中是否存在5个数，使他们能组成公差1的等差数列
# 排序 每5个一组检查


def check(L):
    L.sort()
    lenl = len(L)
    fail = True
    for i in range(lenl-4):
        for j in range(4):
            if L[i+j] + 1 != L[i+j+1]:
                break
            if j == 3:
                fail = False

    return not fail

if __name__ == '__main__':
    while True:
        L = input().split() #5 2 3 4 6 0
        L1 = [int(item) for item in L]
        print(check(L1))