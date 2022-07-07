"""
Plot voltages recorded for the three scripts related to the A123 cell. Data is
read from csv files located in the dyn_data/ folder. The csv files were created
from the mat files located in the Matlab ESCtoolbox at DYN/A123_DYN.
"""

import matplotlib.pyplot as plt
import pandas as pd

# list of csv files based on magnitude and temperature
magtemps = [25, 35, 45]

# choose which group of files to plot, index should be a number from 0-7
mag = magtemps[0]

# plot data from the csv files

plt.ion()
plt.close('all')

file1 = f'../Process_data/Script_data/SW_ME_DYN_T{mag}_1_S1.csv'
df1 = pd.read_csv(file1)
voltage1 = df1['voltage'].values
current1 = df1['current'].values
time1 = df1['time'].values
t1 = (time1 - time1[0])/3600

file2 = f'../Process_data/Script_data/SW_ME_DYN_T{mag}_1_S2.csv'
df2 = pd.read_csv(file2)
voltage2 = df2['voltage'].values
current2 = df2['current'].values
time2 = df2['time'].values
t2 = (time2 - time2[0])/3600

file3 = f'../Process_data/Script_data/SW_ME_DYN_T{mag}_1_S3.csv'
df3 = pd.read_csv(file3)
voltage3 = df3['voltage'].values
current3 = df3['current'].values
time3 = df3['time'].values
t3 = (time3 - time3[0])/3600

# plot voltage from each script

fig = plt.figure()

ax1 = fig.add_subplot(221)
ax1.plot(t1, voltage1, color='red')
ax1.set_title(f'T{mag}_1_S1', fontsize=10)

ax2 = fig.add_subplot(222)
ax2.plot(t2, voltage2, color='red')
ax2.set_title(f'T{mag}_1_S2', fontsize=10)

ax3 = fig.add_subplot(223)
ax3.plot(t3, voltage3, color='red')
ax3.set_title(f'T{mag}_1_S3', fontsize=10)

fig.text(0.5, 0.01, 'Time (hr)', ha='center')
fig.text(0.01, 0.5, 'Voltage (V)', va='center', rotation='vertical')
plt.tight_layout()

# plot current from each script

fig = plt.figure()

ax1 = fig.add_subplot(221)
ax1.plot(t1, current1, color='blue')
ax1.set_title(f'T{mag}_1_S1', fontsize=10)

ax2 = fig.add_subplot(222)
ax2.plot(t2, current2, color='blue')
ax2.set_title(f'T{mag}_1_S2', fontsize=10)

ax3 = fig.add_subplot(223)
ax3.plot(t3, current3, color='blue')
ax3.set_title(f'T{mag}_1_S3', fontsize=10)

fig.text(0.5, 0.01, 'Time (hr)', ha='center')
fig.text(0.01, 0.5, 'Current (A)', va='center', rotation='vertical')
plt.tight_layout()
input()
