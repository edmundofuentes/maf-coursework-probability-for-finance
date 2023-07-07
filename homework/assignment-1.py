import random
import matplotlib.pyplot as plt


# Define a gaussian (normal) random variable
def random_gaussian():
    return sum(random.uniform(0, 1) for i in range(12)) - 6


# Iterate to generate N observations
def normal_distribution(events):
    dist = []
    for i in range(events):
        dist.append(random_gaussian())
    return dist


# Run the simulation for 100,000 cycles
dist = normal_distribution(100000)

# Draw a histogram from the observations
plt.hist(dist, bins=100, range=(-3.1, 3.1))
plt.show()