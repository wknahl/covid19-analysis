# 4817040251 - M. WAHID KHOIRUNNAHL #
import numpy as np
import pandas as pd
from scipy.linalg import lstsq
import matplotlib.pyplot as plt


data = pd.read_csv(r'cov19-ina.csv',
                   usecols=[0, 1, 2, 3, 4], skiprows=1, sep=',', index_col=None, header=None)
# print(data)

Month = np.array(data[0])
Infected = np.array(data[1])
NewCase = np.array(data[2])
RecoverCase = np.array(data[3])
DeathCase = np.array(data[4])

M = Month[:, np.newaxis]**[0, 1]
modelInfected, _, _, _ = lstsq(M, Infected)
modelNewCase, _, _, _ = lstsq(M, NewCase)
modelRecoverCase, _, _, _ = lstsq(M, RecoverCase)
modelDeathCase, _, _, _ = lstsq(M, DeathCase)
print "--------------------------------------"
print "Intercept Total Case=", modelInfected[0]
print "Month Coefficient Total Case =", modelInfected[1]
print "--------------------------------------"
print "Intercept New Case=", modelNewCase[0]
print "Month Coefficient New Case =", modelNewCase[1]
print "--------------------------------------"
print "Intercept Recover Case=", modelRecoverCase[0]
print "Month Coefficient Recover Case =", modelRecoverCase[1]
print "--------------------------------------"
print "Intercept Death Case=", modelDeathCase[0]
print "Month Coefficient Death Case =", modelDeathCase[1]
print "--------------------------------------"

#########################

# ------- Total Infected ------- #
# line 1 points
# y1 = np.array(data[1])
# x1 = ['Maret', 'April', 'Mei', 'Juni']
# # plotting the line 1 points
# plt.plot(x1, y1, label="Maret")

# # naming the x axis
# plt.xlabel('x - axis')
# # giving a title to my graph
# plt.title('Two lines on same graph!')

# # show a legend on the plot
# plt.legend()

# # function to show the plot
# plt.show()

# data = {'Maret': 1528, 'April': 10118, 'Mei': 26473, 'Juni': 55092}
month = ['Maret', 'April', 'Mei', 'Juni']
values1 = np.array(data[1])
values2 = np.array(data[2])
values3 = np.array(data[3])
values3 = np.array(data[4])

fig, axs = plt.subplots(1, 4, figsize=(12, 5), sharey=True)
axs[0].bar(month, values1)
axs[0].set_title('Total Infected', fontsize=9)
axs[1].plot(month, values2)
axs[1].set_title('New Case PerDay', fontsize=9)
axs[2].plot(month, values3)
axs[2].set_title('Recovered Case PerDay', fontsize=9)
axs[3].plot(month, values3)
axs[3].set_title('Death Case PerDay', fontsize=9)

fig.suptitle('Time Series Analysis COVID-19 in Indonesia')

plt.show()
# 4817040251 - M. WAHID KHOIRUNNAHL #
