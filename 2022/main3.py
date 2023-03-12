# 输出大于等于k个字母组合 例如给出abca 给定k=2 输出数列[ab,ac,bc,abc]
# 先去重 再用dfs跑一下

ans = []
def dfs(s1,snow,cur,k,lst):
    if cur == k:
        ans.append(snow)
        return
    lens = len(s1)
    for i in range(lst,lens):
        dfs(s1,snow+s1[i],cur+1,k,i+1)


if __name__ == '__main__':
    s = input()
    k = int(input())
    s1 = ""
    dictz = {}
    for item in s:
        t = dictz.get(item,0)
        if t == 0:
            s1 += item
            dictz[item] = t + 1
    lens = len(s1)
    for i in range(k,lens+1):
        dfs(s1,"",0,i,0)
    print(ans)