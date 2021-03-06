import math
import numpy
import matplotlib.pyplot as pp

# Her er den eksakte løsning:
def rigtig(x):
    return (math.sqrt(6*(x**3) + 30))/3

# Nu laves data til den eksakte løsning:
x_rig = numpy.linspace(1, 100, 10000)
y_rig = []
for i in range(len(x_rig)):
    y_rig.append(rigtig(x_rig[i]))


# Differentialligningerne som skal løses defineres her:
def y_prime(x):
    return x**2


def x_prime(y):
    return y

# Eulers metode:
def euler(y, time, dt, derivs):
    return dt*derivs(y)+y

# Her er udregningerne for den numeriske løsning af de koblede differentialligninger:
x_euler = [1]
y_euler = [2]
dt = 100/1000000000
i = 0
while x_euler[i] < 100:
    y_euler.append(y_euler[i]+dt*y_prime(x_euler[i]))
    x_euler.append(x_euler[i]+dt*x_prime(y_euler[i]))
    i += 1

    
# Her er grafen lavet:
pp.plot(x_rig, y_rig, 'r')
pp.plot(x_euler, y_euler, 'g--')
pp.legend(['Rigtig', 'Numerisk'])
pp.show()


