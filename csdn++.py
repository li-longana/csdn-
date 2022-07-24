from time import sleep
from turtle import end_fill
import main
import time
index=main.Openurl('url.txt').url
print("加载到目标博客。。数量",len(index))
t1=int(input("请设定推广次数“："))-1
t2=int(input("请设定间隔时间\(单位：s，推荐每分钟一次，不要太低，最低不过5秒\)："))
# 加载主页地址
timei=time.perf_counter()
cs=1
z=True
while(z):
    for i in index:
    # 获取当前博主的所有文章
        temp=main.indexurl(i).url

        # 开始推广

        
        for j in temp:
            main.gogogo(j)
            sleep(t2)# 冷却时间
            cs=cs+1
            timen=(t1-cs)*t2
            print("推广次数",cs,"预计剩余时间：",timen,end="")
            if cs>t1:
                cs=0
                z=False
                print()
                timei=int(time.perf_counter())-int(timei)
                print("完成,共耗时：",timei)
                break
            else:
                print(end="\r")
        

