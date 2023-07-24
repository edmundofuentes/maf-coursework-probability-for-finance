import math

# install numpy first by running: pip3 install numpy
import numpy as np

# install matplotlib first by running: pip3 install matplotlib
import matplotlib.pyplot as plt

print('Milstein Discretization - Simulation - Stochastic Differential Equation')

def milstein_simulation(numberOfTrajectories, numberOfSteps):
    # Number of trajectories by series
    # Number of step to simulate

    # Initial Parameters
    x0 = 100 # precio inicial
    a = 0.05 # tasa de apreciación (para el periodo)
    b = 0.20 # volatilidad (peso del movimiento browniano)

    # ∆t
    dT = 1 / numberOfSteps
    sqrtDT = math.sqrt(dT)

    #print(f'∆t = {dT}')
    #print(f'√∆t = {math.sqrt(dT)}')

    # Computation of the Gaussian Variables
    # multiply the scalar sqrt(∆t) by a matrix of randomly generated elements using a normal (gaussian) distribution
    # brownian motion requires a _variance_ of ∆t for the set.
    # multiplying a normal matrix by a scalar will make the std.dev. (µ) equal the scalar,
    # so we multiply by √∆t to obtain the variance
    dW = math.sqrt(dT) * np.random.normal(size=(numberOfTrajectories, numberOfSteps+1))
    # print(dW)

    # Initialize the trajectories matrix
    # this creates a matrix of zeroes of shape:
    # - rows: numberOfTrajectories
    # - cols: numberOfSteps + 1
    trajectories = np.zeros((numberOfTrajectories, numberOfSteps+1))

    # set the first element of all trajectories to equal x0
    # the value of x0 is our initial value for all trajectories
    for traj in trajectories:
        traj[0] = x0

    # Loop and simulate all steps
    for i in range(numberOfTrajectories):
        for t in range(numberOfSteps):
            factor = 1 + (a * dT) + (b * dW[i][t]) + ((1/2) * (b**2) * ((dW[i][t]**2) - dT))
            trajectories[i][t+1] = trajectories[i][t] * factor

    # print(trajectories)

    for traj in trajectories:
        plt.plot(traj)

    plt.show()

milstein_simulation(10, 10)
