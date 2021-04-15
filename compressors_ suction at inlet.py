import math
import cmath
import matplotlib.pyplot
import random
import turtle
import time

print('insert target flow rate m_dot[kg/s]')
m=float(input())

print('insert p10[bar]')
p10=float(input())


print('insert T1[K]')
T1=float(input())

print('insert T10[K]')
T10=float(input())

print('insert p2[bar]')
p2=float(input())

print('lets start the iterative process')

while(1):
    print ( 'insert p1 guess[bar]' )
    p1 = float ( input ( ) )

    m_reduced= m*math.sqrt(T1/T10)/p1/p10
    print('m_reduced= '+str(m_reduced)+'\n inserire il valore di beta corrispondente')

    beta= float(input())

    print('p1_found= '+str(p2/beta))
    difference =math.fabs(p1-p2/beta)
    print('difference between guessed and graph p1= '+str(difference))

    if(difference<0.01):
        print('p1 found! \n p1= '+str(p1))
        print('beta= '+str(beta))
        print('m_reduced= '+str(m_reduced))
        print('iterative process ended succesfully')
        break
    else:
        if(p1-p2/beta<0):
            print('aumenta p1')
        else:
            print('diminuisci p1')
        print('convergence not achieved yet')



