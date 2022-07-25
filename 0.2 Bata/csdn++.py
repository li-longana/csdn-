import main
import time
print("CSDN++ 0.2 Bata版本启动中。。",end="\r")
time.sleep(1)
print("CSDN++ 0.2 Bata版本启动中。。。。",end="\r")
time.sleep(1)
print("CSDN++ 0.2 Bata版本启动中。。。。。。")
time.sleep(1)
config=main.Openconfig('0.2 Bata\\config.txt').config
# 加载配置文件
print("配置文件加载成功。。。。。")
time.sleep(1)
print("预设推广次数为：",config['count'],"\n预设推广时间间隔为：",config['interval'],"\n预设推广地址为：",config['url'])
time.sleep(1)

ua=main.Openua('0.2 Bata\\ua.txt').ua
# 加载ua
url=main.indexurl(config['url']).url
# 加载文章
timei=time.perf_counter()
z=True
while(z):
    cs=0
    for i in ua:
        for j in url:
            main.gogogo(j,i)
            time.sleep(int(config['interval']))# 冷却时间
            cs=cs+1
            timen=(int(config['count'])-cs)*int(config['interval'])
            print("推广次数",cs,"预计剩余时间：",timen,end="")
            if cs>int(config['count']):
                cs=0
                z=False
                print()
                timei=int(time.perf_counter())-int(timei)
                print("完成,共耗时：",timei)
                break
            else:
                print(end="\r")
