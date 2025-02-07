# -*- coding: utf-8 -*-
# """Untitled17.ipynb

# Automatically generated by Colab.

# Original file is located at
#     https://colab.research.google.com/drive/1gKJWul0hOWZ1oXJoX2A1TVz64jfNXj-b

# Without considering any losses as well as generator limits
# """

import numpy as np

alpha = np.array([500, 400, 200])
beta = np.array([5.3, 5.5, 5.8])
gamma = np.array([0.004, 0.006, 0.009])

PD = 975
Delp = 10

# Error in Delp is set to a high value
lambda_val = float(input('Enter estimated value of Lambda = '))

print(' Lambda P1 P3 DP...grad Delambda')

iter = 0
DelP = 1  # Initialize DelP
P = []
J = 0
Delambda = 0


while abs(DelP) > 0.001:
    iter += 1

    P = (lambda_val - beta) / (2 * gamma)

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
