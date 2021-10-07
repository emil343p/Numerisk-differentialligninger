import numpy as np
import matplotlib.pyplot as pp


# Her er eulers metode:
def euler(y, x, dt, derivs):
    return dt*derivs(y, x)+y


# Så kan man begynde at løse differential ligningerne
# Her er konstanter:
alpha = 0.3 # Gennemsnitlige albedo (intensiteten af tilbagekastet lys)
sigma = 5.67 * 10**(-8) # Stefan-Boltzmann konstant
S = 342 # Gennemsnitlige energi fra Solen pr. område
epsilon = 0.8 # Emmission fra grå krop

# Her er differentialligningerne som skal løses:
def diff_t_p(t_p, t_a):
    return ((1-alpha)*S-sigma*(t_p**4))+epsilon*sigma*(t_a**4)


def diff_t_a(t_p, t_a):
    return epsilon*sigma*(t_p**4) - (2*epsilon*sigma*(t_a**4))


# Så kan man begynde at udregne det:
# Man starter med at lave x-aksen, som har tid:
length = 5
steps = 10000
time = np.linspace(0, length, steps)
# Her klargøres listerne som bruges til selve udregningerne:
t_p = [0]*steps
t_a = [0]*steps
# Startbetingelser:
t_p[0] = 200
t_a[0] = 300


# Man begynder med differentialligningerne:
i = 1
while i < steps:
    t_p[i] = (euler(t_p[i-1], t_a[i-1], length/steps, diff_t_p)) # Man "opdatere" t_p
    t_a[i] = (t_a[i-1]+(length/steps) * (epsilon*sigma*t_p[i-1]**4 - 2*epsilon*sigma*t_a[i-1]**4)) # Man "opdatere" t_a
    i += 1



# Her er linjerne for temperatur:
pp.plot(time, t_p, 'g')
pp.plot(time, t_a, 'b')
# Her er linjerne for ligevægt:
pp.hlines(t_p[steps-1], -0.5, 5.5, colors='k', linestyles='--')
pp.hlines(t_a[steps-1], -0.5, 5.5, colors='k', linestyles='--')
pp.text(1.5, t_p[steps-1]+7, rf'$T_p$ = {round(t_p[steps-1])} K')
pp.text(1.5, t_a[steps-1]+7, rf'$T_a$ = {round(t_a[steps-1])} K')
# Her er resten:
pp.legend(['Jorden', 'Atmosfæren'])
pp.xlabel('Tid')
pp.ylabel('Temperatur (K)')
pp.title('En simpel klimamodel')
pp.xlim((-0.1, 5))
pp.show()
