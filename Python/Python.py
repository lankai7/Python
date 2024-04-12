###############################################
# 设计 July_Lankai     创建 2023-10-12         #
# turtle 绘简笔画                              #
###############################################
from os import write
import turtle as tl
tl.speed(0)			# 设置最快绘图速度
tl.setup(780, 650)		# 设置画面尺寸
tl.title('那就给天诺画一个吧')
tl.pu()
R = 1/3				# 设置比例因子, 用数据的1/3大小绘制
x0, y0 = R*1250, R*1000		# 设置位置偏移量, 使图像处于窗口中间
tl.pensize(4)   #笔的粗细

tl.pu()
tl.goto(-71,4)      #左侧手臂
tl.pd()
tl.color('black','#FF1493') 
tl.right(170) 
tl.begin_fill()
tl.circle(350*R, 25)
tl.left(61)
tl.circle(120*R, 50)
tl.end_fill()


tl.pu()
tl.goto(-77,0)    #身子
tl.setheading(0)
tl.color('black','#87CEFA') 
tl.right(130)
tl.pd()
tl.begin_fill()
tl.circle(350*R, 35)
tl.circle(140*R, 95)
tl.forward(48)
tl.circle(140*R, 95)
tl.circle(350*R, 33)
tl.end_fill()


tl.pu()     
tl.goto(6,-28)      #衣服两个白洞右
tl.color('black','white') 
tl.pd()
tl.begin_fill()
tl.circle(10)
tl.end_fill()

tl.pu()             #衣服两个白洞左
tl.goto(-62,-28)
tl.color('black','white') 
tl.pd()
tl.begin_fill()
tl.circle(10)
tl.end_fill()

tl.pu()
tl.goto(0,0)    #身子
tl.setheading(0)
tl.color('black','pink') 
tl.pd()
tl.left(145)
tl.begin_fill()			# 杯子填色开始
tl.circle(200*R, 70)		# 画杯子起笔
tl.left(50)
tl.circle(250*R, 30)        #杯左壁
tl.circle(50*R, 50)         #杯底
tl.circle(200*R, 35)
tl.left(10)
tl.circle(100*R, 15)        #杯子右壁
tl.circle(75*R, 30)
tl.right(90)
tl.circle(50*R, 200)         #杯子把
tl.end_fill()
tl.pu()
tl.goto(-2,-26)
tl.pd()
tl.fillcolor('white')
tl.begin_fill()     #杯子把出漏洞填充
tl.right(190)
tl.circle(25*R, 180)  
tl.goto(-2/3*R,-25)
tl.end_fill()              #杯子外形完

tl.pu()
tl.goto(-38,-38)    #杯上爱心#杯上爱心
tl.pd()
tl.color('#FF69B4')
tl.begin_fill()     
tl.setheading(0)
tl.left(140)
tl.forward(12)
tl.circle(-6, 200)
tl.setheading(60)
tl.circle(-6, 200)
tl.forward(12)
tl.end_fill() 

tl.pu()
tl.color('black','white')   #杯子内部
tl.goto(-8,-4)
tl.setheading(0)
tl.left(150)
tl.pd()
tl.begin_fill()
tl.circle(180*R, 60)
tl.pu()
tl.goto(-8,-4)
tl.setheading(0)
tl.right(150)
tl.pd()
tl.circle(-180*R, 60)
tl.end_fill() 

tl.pu()
tl.goto(0,0)        #头部外形
tl.setheading(0)
tl.left(5)
tl.pd()
tl.circle(320*R, 30)
tl.circle(200*R, 100)
tl.right(70)
tl.circle(250*R, 40)
tl.circle(30*R, 80)
tl.circle(250*R, 40)
tl.right(70)
tl.circle(280*R, 50)
tl.right(70)
tl.circle(250*R, 40)
tl.circle(30*R, 80)
tl.circle(250*R, 40)
tl.right(70)
tl.circle(200*R, 122)
tl.circle(500*R, 10)


tl.pu()
tl.goto(-119,-12)   #左手
tl.setheading(0)
tl.left(122)
tl.pd()
tl.circle(36*R, 180)
tl.right(90)
tl.circle(80*R, 190)


tl.pu()
tl.goto(5,-10)    #右侧手臂
tl.color('black','white') 
tl.setheading(0)
tl.left(85)
tl.pd()
tl.begin_fill()
tl.circle(-70*R, 180)
tl.circle(-120*R, 40)
tl.circle(-80*R, 50)
tl.circle(-40*R, 80)
tl.right(3)
tl.circle(400*R, 10)
tl.end_fill()


tl.pu()
tl.goto(-55,-115)   #左脚
tl.color('black','white') 
tl.setheading(0)
tl.left(60)
tl.pd()
tl.begin_fill()
tl.circle(121*R, 150)
tl.circle(60*R, 30)
tl.circle(121*R, 150)
tl.circle(60*R, 30)
tl.end_fill()

tl.pu()
tl.goto(-15,-115)   #右脚
tl.color('black','white') 
tl.setheading(0)
tl.right(240)
tl.pd()
tl.begin_fill()
tl.circle(-121*R, 150)
tl.circle(-60*R, 30)
tl.circle(-121*R, 150)
tl.circle(-60*R, 30)
tl.end_fill()


tl.pu()
tl.goto(-90,68)   #左眼睛
tl.color('black','black') 
tl.setheading(0)
tl.right(78)
tl.pd()
tl.begin_fill()
tl.circle(-60*R, 35)
tl.circle(-16*R, 145)
tl.circle(-60*R, 35)
tl.circle(-16*R, 145)
tl.end_fill()

tl.pu()
tl.goto(28,65)   #右眼睛
tl.color('black','black') 
tl.setheading(0)
tl.right(80)
tl.pd()
tl.begin_fill()
tl.circle(-60*R, 35)
tl.circle(-16*R, 145)
tl.circle(-60*R, 35)
tl.circle(-16*R, 145)
tl.end_fill()


tl.pu()
tl.goto(-47,45)   #鼻子
tl.color('black','yellow') 
tl.setheading(0)
tl.left(30)
tl.pd()
tl.begin_fill()
tl.circle(-60*R, 50)
tl.circle(-16*R, 130)
tl.circle(-60*R, 50)
tl.circle(-16*R, 130)
tl.end_fill()

tl.pu()
tl.goto(62,74)   #右侧胡子1
tl.color('black') 
tl.setheading(0)
tl.left(20)
tl.pd()
tl.circle(-180*R, 30)
tl.circle(-260*R, 11)

tl.pu()
tl.goto(62,52)   #右侧胡子2
tl.color('black') 
tl.setheading(0)
tl.left(5)
tl.pd()
tl.circle(-260*R, 24)

tl.pu()
tl.goto(48,32)   #右侧胡子3
tl.color('black') 
tl.setheading(0)
tl.right(5)
tl.pd()
tl.circle(-260*R, 26)

tl.pu()
tl.goto(-134,78)   #左侧胡子1
tl.color('black') 
tl.setheading(180)
tl.right(15)
tl.pd()
tl.circle(260*R, 25)
tl.circle(180*R, 12)

tl.pu()
tl.goto(-134,56)   #左侧胡子2
tl.color('black') 
tl.setheading(180)
tl.right(5)
tl.pd()
tl.circle(260*R, 23)

tl.pu()
tl.goto(-122,36)   #左侧胡子3
tl.color('black') 
tl.setheading(180)
tl.left(5)
tl.pd()
tl.circle(260*R, 29)


tl.pu()
tl.goto(-122,36)   #蝴蝶结
tl.color('black') 
tl.setheading(180)
tl.left(5)
tl.pd()
tl.circle(260*R, 29)



#tl.hideturtle()
tl.done()