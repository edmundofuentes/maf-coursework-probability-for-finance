import math
import matplotlib.pyplot as plt
import numpy as np


# Multiplicative Binominal Distribution
# Input: initial value, percent change per step, number of steps
def dist_bin_mult(initialValue, percentChange, steps):
    out = []
    prob = []

    for k in range(steps+1):
        # calculate the possible prices
        w = initialValue * ((1+percentChange)**k) * ((1-percentChange)**(steps-k))

        # calculate the probability
        p = math.comb(steps, k) * (1/2**steps)

        out.append(w)
        prob.append(p)

    return [out, prob]


out, prob = dist_bin_mult(10, 0.05, 20)

# bar(x, y (height)) where
plt.bar(out, prob, width=0.4)

# configure the axis of the plot
plt.xlim((0, 27))
plt.xticks(np.arange(0, 27, step=2))
plt.ylim((0, 0.20))

# display the graph
plt.show()


