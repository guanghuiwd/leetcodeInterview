
# 来源：牛客网

n,m,c=map(int,input().split())

save=[]
#都放数组里面
for i in range(n):
    save.append([int(i) for i in input().split()][1:])
save
#统计的是颜色!从题目上看到color很小,所以for 按照c的值来.
memo={}

#遍历所有珠子,遇到一个颜色就给他的index存到memo字典里面存成一个数组然后
#当这个数组长度大于1时候判断里面是否有index距离小于m.

count=0
for i in range(1,c+1):
    tmp=[]#记录颜色i的index.
    for j in range(n):
        if i in save[j]:
            tmp.append(j)
        if len(tmp)>=2  :
            if  tmp[-1]-tmp[-2]<m or n+tmp[0]-tmp[-1]<m:
                count+=1
                break
print(count)
