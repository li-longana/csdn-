import main
import time
import random
print("CSDN++ 0.2 Bata版本启动中。。",end="\r")
time.sleep(1)
print("CSDN++ 0.2 Bata版本启动中。。。。",end="\r")
time.sleep(1)
print("CSDN++ 0.2 Bata版本启动中。。。。。。")
time.sleep(1)
config=main.Openconfig('config.txt').config
# 加载配置文件
print("配置文件加载成功。。。。。")
time.sleep(1)
print("预设推广次数为：",config['count'],"\n预设推广时间间隔为：",config['interval'],"\n预设推广地址为：",config['url'])
time.sleep(1)
luck=random.randint(1,100)
print("你的幸运值为：",luck)
ua=main.Openua('ua.txt').ua
# 加载ua

timei=time.perf_counter()
z=True
while(z):
    url = main.indexurl(config['url']).url
    # 加载文章
    cs=0
    for j in url:
        uatemp=ua[cs%(len(ua)+luck)]
        main.gogogo(j,uatemp)
        time.sleep(int(config['interval']))# 冷却时间
        cs=cs+1
        timen=(int(config['count'])-cs)*int(config['interval'])
        print("\r推广次数",cs,"预计剩余时间：",timen,end="")
        if cs>int(config['count']):
            cs=0
            z=False
            print()
            timei=int(time.perf_counter())-int(timei)
            print("完成,共耗时：",timei)
            break
