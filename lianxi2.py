import math
#返回多个值
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

inputx=int(input('请输入横坐标：'))
inputy=int(input('请输入纵坐标：'))
inputstep=int(input('请输入位移：'))
inputangle=math.pi/int(input('请输入角度:'))
x,y=move(inputx,inputy,inputstep,inputangle)
print('这个点位移后的坐标是：%d,%d'%(x,y))#其实返回值是tuple