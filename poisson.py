import random
import math
# install bashplotlib first by running:  pip3 install bashplotlib
from bashplotlib.histogram import plot_hist

print('Poisson distribution')

def poisson_dist(lmb):
    debug = True # set to True to print out each step of the process
    x = 0
    u = random.uniform(0, 1)

    if debug: print(f"Randomize X for λ = {lmb}; e^(-λ) = { str(math.exp(-lmb))}")
    if debug: print(f"X{str(x)} U1: {str(u)} Π(U): {str(u)}")

    while u >= math.exp(-lmb):
        x = x + 1
        un = random.uniform(0, 1)
        u = u * un

        if debug: print(f"X{str(x)} U{str(x+1)}: {str(un)} Π(U): {str(u)}")

    if debug: print(f"X = {x}")

    return x

poisson_dist(4)
exit(0)

def poisson_prob(lmb, k):
    return math.exp(-lmb) * math.pow(lmb, k) / math.factorial(k)


lmb = 4

print(f"Simulate Distribution with λ = {lmb}")

#x = poisson(4)
#print('')
#print('X = ' + str(x))

x = []

for i in range(10000):
    x.append(poisson_dist(lmb))

plot_hist(x, showSummary=True)

k = 7
print(f"Find Probability that X = {k} (k={k}) with λ = {lmb}")
print('Calculated probability:')
print(poisson_prob(lmb, k))

n = 0
for i in x:
    if i == k:
        n += 1

print('Simulation result:')
print(n / len(x))

