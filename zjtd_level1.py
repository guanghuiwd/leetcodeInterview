n = int(input())
li = [int(a) for a in input().split()]
d = {}
for i,v in enumerate(li):
    if v not in d:
        d[v] = [i + 1]
    else:
        d[v].append(i+1)
q = int(input())
for _ in range(q):
    l, r, k = map(int, input().split())
    if k not in d.keys():
        print(0)
    else:
        a = 0
        for j in d[k]:
            if j>=l and j<=r:
                a += 1
        print(a)
        
# 就是用最抽象的几个数字完成含义设置，完成一个简单的问题。
