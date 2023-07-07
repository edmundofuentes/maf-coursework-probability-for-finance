import random
import math
import matplotlib.pyplot as plt

def gaussian(scale=2):
    return sum(random.uniform(0, 1) for i in range(scale)) - (scale/2.0)


def dist_normal_m1(events, scale):
    res = []
    for i in range(events):
        x = gaussian(scale)
        res.append(x)
    return res


# µ = 0 (media)
# σ = 1 (varianza)
def std_norm_dist(z):
    return math.exp(-1 * (z**2) / 2) / math.sqrt(2 * math.pi)


n100 = dist_normal_m1(100000, 12)
#print(n100)

plt.hist(n100, bins=50, range=(-3, 3))
#plt.show()

normal_x = []
normal_y = []
normal_steps = 100
step = 6 / normal_steps
for i in range(normal_steps):
    ix = (i * step) - 3
    iy = std_norm_dist(ix)
    #print(f"{ix} {iy}")
    normal_x.append(ix)
    normal_y.append(iy)

#print(normal)
plt.plot(normal_x, normal_y)
plt.show()


x = sum(random.uniform(0, 1) for i in range(12)) - 12/2
print(x)

