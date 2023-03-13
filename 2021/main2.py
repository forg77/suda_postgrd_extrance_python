# 找到列表中某一元素后比该元素大的数 满足i<j 且 L[i]<L[j] 且j尽可能小 没有满足条件的数则用None表示
# L[5,2,3] 返回 [None,3,None] ; L[2,3,5] 返回 [3,5,None]
# 很直觉的n^2解法

if __name__ == '__main__':
    while True:
        L = input().split()
        L1 = [int(item) for item in L]
        ans = []
        lenl = len(L1)
        for i in range(lenl):
            fail = True
            for j in range(i+1,lenl):
                if L1[j] > L1[i]:
                    ans.append(L1[j])
                    fail = False
                    break
            if fail:
                ans.append(None)
        print(ans)