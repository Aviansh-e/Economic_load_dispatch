# """considering Genrator limits"""

import numpy as np

alpha = np.array([500, 400, 200])
beta = np.array([5.3, 5.5, 5.8])
gamma = np.array([0.004, 0.006, 0.009])
lower_bound = np.array([200, 150, 100])
upper_bound = np.array([450, 350, 225])

PD = 975
Delp = 10

# Error in Delp is set to a high value
lambda_val = float(input('Enter estimated value of Lambda = '))

print(' Lambda P1 P3 DP...grad Delambda')

iter = 0
DelP = 1  # Initialize DelP
P = lower_bound.copy()+1
J = 0
Delambda = 0


def check1():

    for i in range(len(P)):
        if (P[i] < lower_bound[i]):
            return True
    for i in range(len(P)):
        if (P[i] > upper_bound[i]):
            return True
    return False


while abs(DelP) > 0.001 or check1():
    iter += 1

    P = (lambda_val - beta) / (2 * gamma)

    # Clip P values to be within the bounds
    # P = np.clip(P, lower_bound, upper_bound)

    for i in range(len(P)):
        if (P[i] > upper_bound[i]):
            P[i] = upper_bound[i]

    for i in range(len(P)):
        if (P[i] < lower_bound[i]):
            P[i] = lower_bound[i]

    DelP = PD - np.sum(P)

    J = np.sum(1 / (2 * gamma))  # Gradient sum

    Delambda = DelP / J

    lambda_val += Delambda

if DelP <= 0.001:
    print([lambda_val])
    for i in P:
        print(i, end=' ')
    print(DelP, J, Delambda)
totalcost = np.sum(alpha + beta * P + gamma * P**2)
print('Total fuel cost will be consumed :', totalcost, '$/hour')
