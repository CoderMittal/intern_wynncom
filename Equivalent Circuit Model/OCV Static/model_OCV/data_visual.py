"""
Plot the data from the four A123 battery tests conducted at a range of
temperatures. Change the tc variable to view plots from the other test data.
For example, change the tc string to N05 to create plots for the CSV files
named A123_OCV_N05_S1, A123_OCV_N05_S2, A123_OCV_N05_S3, and A123_OCV_N05_S4.
"""

import matplotlib.pyplot as plt
import pandas as pd

# Data
# ------------------------------------------------------------------------------

# string that represents temperature of battery test to determine which csv
# files to read, values can be N05, N15, N25, P05, P15, P25, P35, or P45
tc = '25'
Cell = 'C6411'

df1 = pd.read_excel('../process_data/Script_data/SW_ME_ST_T'+tc+'_1_S1.xlsx')
test_time1 = df1['Test_Time(s)']
current1 = df1['Current(A)']
voltage1 = df1['Voltage(V)']

df2 = pd.read_excel('../process_data/Script_data/SW_ME_ST_T'+tc+'_1_S2.xlsx')
test_time2 = df2['Test_Time(s)']
current2 = df2['Current(A)']
voltage2 = df2['Voltage(V)']

df3 = pd.read_excel('../process_data/Script_data/SW_ME_ST_T'+tc+'_1_S3.xlsx')
test_time3 = df3['Test_Time(s)']
current3 = df3['Current(A)']
voltage3 = df3['Voltage(V)']

df4 = pd.read_excel('../process_data/Script_data/SW_ME_ST_T'+tc+'_1_S4.xlsx')
test_time4 = df4['Test_Time(s)']
current4 = df4['Current(A)']
voltage4 = df4['Voltage(V)']

# Compare Temperature Data
# ------------------------------------------------------------------------------

temps = ['25', '35', '45']
times = []
volts = []

for t in temps:
    df = pd.read_excel('../process_data/Script_data/SW_ME_ST_T' + t + '_1_S1.xlsx')
    time = df['Test_Time(s)'].values
    voltage = df['Voltage(V)'].values
    times.append(time)
    volts.append(voltage)

# for t in temps:

# Plot
# ------------------------------------------------------------------------------

plt.ion()
plt.close('all')

# Figure 1
plt.figure(1)
plt.plot(times[0], volts[0], label='25$^{\circ}$C')
plt.plot(times[1], volts[1], label='35$^{\circ}$C')
plt.plot(times[2], volts[2], label='45$^{\circ}$C')
plt.legend(loc='best')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title(Cell)
input("Press Enter to Continue")
# Figure 2
fig, ax1 = plt.subplots()
plt.title(Cell  + '_T'+ tc + '_S1')

ax1.plot(test_time1, current1, color='b', lw=2, label='current')
ax1.set_xlabel('Test Time (s)')
ax1.set_ylabel('Current (A)', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(test_time1, voltage1, color='r', lw=2, label='voltage')
ax2.set_ylabel('Voltage (V)', color='r')
ax2.tick_params('y', colors='r')
fig, ax1 = plt.subplots()
plt.title(Cell + '_T' + tc + '_S2')

ax1.plot(test_time2, current2, color='b', lw=2, label='current')
ax1.set_xlabel('Test Time (s)')
ax1.set_ylabel('Current (A)', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(test_time2, voltage2, color='r', lw=2, label='voltage')
ax2.set_ylabel('Voltage (V)', color='r')
ax2.tick_params('y', colors='r')
fig, ax1 = plt.subplots()
plt.title(Cell + '_T' + tc + '_S3')

ax1.plot(test_time3, current3, color='b', lw=2, label='current')
ax1.set_xlabel('Test Time (s)')
ax1.set_ylabel('Current (A)', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(test_time3, voltage3, color='r', lw=2, label='voltage')
ax2.set_ylabel('Voltage (V)', color='r')
ax2.tick_params('y', colors='r')
fig, ax1 = plt.subplots()
plt.title(Cell + '_T' + tc + '_S4')

ax1.plot(test_time4, current4, color='b', lw=2, label='current')
ax1.set_xlabel('Test Time (s)')
ax1.set_ylabel('Current (A)', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(test_time4, voltage4, color='r', lw=2, label='voltage')
ax2.set_ylabel('Voltage (V)', color='r')
ax2.tick_params('y', colors='r')
input("Press Enter to Continue")