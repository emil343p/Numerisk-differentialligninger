import math
import numpy
import matplotlib.pyplot as pp

# Eulers metode:
def euler(y, time, dt, derivs):
    return dt*derivs(y)+y

# Her er differentialligningen:
def deriv(x, y):
    return x+y

# Den rigtige løsning, som vi sammenligner med. f(0)=2
def rigtig(x):
    return -x-1+3*math.exp(x)


# Her laves data til den eksakte løsning
x_rig = numpy.linspace(0, 100, 10000)
y_rig = []
for i in range(len(x_rig)):
    y_rig.append(rigtig(x_rig[i]))

# Med eulers metode laver man data:
x_euler = numpy.linspace(0, 100, 10000000)
y_euler = [2]
i = 1
while i < 10000000:
    y_euler.append(y_euler[i-1]+100/10000000 * deriv(x_euler[i-1], y_euler[i-1]))
    i += 1


# Her laves grafer
pp.plot(x_rig, y_rig)
pp.plot(x_euler, y_euler)
pp.legend(['Rigtig', 'Euler', 'RK'])
pp.show()
