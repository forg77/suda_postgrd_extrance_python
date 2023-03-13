# 给定一个列表L 列表中元素均为{1,2,3,4,5,6,7,8,9,0}的子集，从该列表中找出一个元素 若该元素出现的次数大于 len(L)/2 则返回该元素 否则返回None
# set 转 tuple 用dict存储 遍历找出符合要求的集合


def solve(lst):
    dictz = {}
    lenl = len(lst)
    for item in lst:
        dictz[tuple(item)] = dictz.get(tuple(item),0) + 1
    ans = []
    for item in dictz.keys():
        if dictz[item] > lenl / 2:
            ans.append(set(item))
    if len(ans) == 0:
        return None
    return ans


if __name__ == '__main__':
    Testcase1 = [{1},{1,3},{1}]
    Testcase2 = [{3,2},{2,4},{3,4},{2,3}]
    Testcase3 = [{3,1,2},{2,2},{1,2,3}]
    ansk = solve(Testcase3)
    print(ansk)