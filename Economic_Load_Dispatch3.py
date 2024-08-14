
# """Considering losses as well as genrator limits"""


alpha = np.array([200, 180, 140])
beta = np.array([7.0, 6.3, 6.8])
gamma = np.array([0.008, 0.009, 0.007])
lower_bound = np.array([10.0, 10.0, 10.0])
upper_bound = np.array([85, 80, 70])

B = np.array([[0.0218, 0.0, 0.0],
              [0.0, 0.0228, 0.0],
              [0.0, 0.0, 0.0179]])    # associated with p1^2,p2^2,p2^2.. this is the function of the power losses with the generators

# this is the coefficients of the power losses
B_O = np.array([7.0, 6.3, 6.8])

# convert the given power losses(B) in MW from Per_Unit

B *= 0.01
PD = 150
DelP = 10

# Error in Delp is set to a high value
lambda_val = float(input('Enter estimated value of Lambda = '))

print(' Lambda P1 P3 DP...grad Delambda')

iter = 0
P = lower_bound.copy()-1

# initially consider power losses as 0;
Power_loss = 0.0
J = 0


def checki():

    for i in range(len(P)):
        if (P[i] < lower_bound[i]):
            return True
    for i in range(len(P)):
        if (P[i] > upper_bound[i]):
            return True
    return False


while checki():  # check() or abs(DelP)>=0.001
    iter += 1
    for i in range(len(P)):
        P[i] = (lambda_val-B_O[i]) / \
            (2*(gamma[i] + lambda_val*B[i][i]))  # eq 7.70
    # calculating power losses
    for i in range(len(P)):
        Power_loss += B[i][i]*pow(P[i], 2)
    DelP = PD + Power_loss - np.sum(P)
    # now it's time to find the value of the lembada
    for i in range(len(P)):
        J += (gamma[i]+B[i][i]*B_O[i])/(2*(gamma[i] +
                                           lambda_val*B[i][i])*(gamma[i]+lambda_val*B[i][i]))
    # print(J)

    Delambda = DelP / J
    print(Delambda)
    lambda_val += Delambda
    # print(lambda_val)

for i in P:
    print(i, end=' ')
print(DelP, J, Delambda)
totalcost = np.sum(alpha + beta * P + gamma * P**2)
print('Total fuel cost will be consumed :', totalcost, '$/hour')
