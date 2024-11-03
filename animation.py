    

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 5)

## convert degree to radian
def radian( degree ):
    return float(degree)* np.pi / 180.

# arms lenght
arm1_len= 6.7
arm2_len=3.4

## read datas


start_arms_degree = np.loadtxt("./question1/start_arms_degree.txt")
end_arms_degree = np.loadtxt("./question1/end_arms_degree.txt")
objectss = np.loadtxt("./question1/cspace_objects.txt")
conf_space_obs = np.loadtxt("./question1/conf_space_obs.txt")


def draw_arm( arms_degree ):
    x0 = 0
    y0 = 0
    
    x1 = arm1_len * np.cos( radian (arms_degree[0] ) )
    y1 = arm1_len * np.sin( radian (arms_degree[0] ) )

    x2 = x1 + ( np.cos( radian( arms_degree[0] + arms_degree[1] ) ) * arm2_len )
    y2 = y1 + ( np.sin( radian( arms_degree[0] + arms_degree[1] ) ) * arm2_len )

    plt.plot ( [ x0 , x1 , x2 ] , [ y0 , y1 , y2 ] , color = 'r')

 

sample_rate=100
conf_xs = np.linspace(  start_arms_degree[ 0 ] , end_arms_degree[0]-365 , num = sample_rate )
conf_ys = np.linspace(  start_arms_degree[ 1 ] , end_arms_degree[1] , num = sample_rate )
cx1=[]
cx2=[]
cy1=[]
cy2=[]
for i in range(sample_rate):
    plt.clf()
    plt.subplot(1,2,2)
    plt.plot(conf_space_obs.T[0],conf_space_obs.T[1], '.')
    plt.xlim(0,364)
    if ( conf_xs[i] < 0 ):
        cx2.append( conf_xs[i]+365 )
        cy2.append( conf_ys[i] )
        plt.plot(cx1 , cy1 , color='r')
        plt.plot(cx2 , cy2 , color='r')
    else:
        cx1.append( conf_xs[i] )
        cy1.append( conf_ys[i] )
        plt.plot(cx1 , cy1 , color='r')
    
    plt.subplot(1,2,1)
    plt.plot(objectss.T[0] , objectss.T[1], '.')
    if ( conf_xs[i] < 0 ):
        draw_arm( [ conf_xs[i]+365 , conf_ys[i] ] )
    else:
       draw_arm( [ conf_xs[i] , conf_ys[i] ] ) 
    plt.pause(0.01)
plt.show()