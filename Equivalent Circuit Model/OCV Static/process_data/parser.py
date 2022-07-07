import pandas as pd
import numpy as np

# Enter the file Name over Here
File_Name = './SW_ME_ST_T25_1.xlsx'
Sheet = 'record'
############################


df = pd.read_excel(io=File_Name, sheet_name=Sheet)
df['Test_Time(s)'] = df['Total Time'].str.split(':').apply(lambda x: int(x[0])*60*60 + int(x[1])*60 + int(x[2]))
df['Test_Time(s)'] = (df['Test_Time(s)']-df['Test_Time(s)'][0])
pd.set_option('use_inf_as_na', True)
df['dV/dt(V/s)'] = ((df['Voltage(V)'].diff())/(df['Test_Time(s)'].diff())).fillna(0)
df.rename(columns = {'Cycle ID':'Cycle_Index','Chg Cap(Ah)':'Charge_Capacity(Ah)', 'DChg Cap(Ah)':'Discharge_Capacity(Ah)','Chg Eng(Wh)':'Charge_Energy(Wh)','DChg Eng(Wh)':'Discharge_Energy(Wh)','Real Time':'Date_Time'}, inplace = True)


# For S1
df_copy = df.iloc[:0,:].copy()
d2 = (df.loc[df['Step ID']==2]).copy()
d2 = df_copy.append(d2, ignore_index=True)
d2['Step_Index']=1
d2['Step_Time']=d2['Test_Time(s)']-d2['Test_Time(s)'][0]
d3 = (df.loc[df['Step ID']==3]).copy()
d3 = df_copy.append(d3, ignore_index=True)
d3['Step_Index']=2
d3['Step_Time']=d3['Test_Time(s)']-d3['Test_Time(s)'][0]
d4 = (df.loc[df['Step ID']==4]).copy()
d4 = df_copy.append(d4, ignore_index=True)
d4['Step_Index']=3
d4['Step_Time']=d4['Test_Time(s)']-d4['Test_Time(s)'][0]
dr = d2.append([d3, d4], ignore_index=True)
dS1 = dr[['Test_Time(s)','Date_Time','Step_Time','Step_Index','Cycle_Index','Current(A)','Voltage(V)','Charge_Capacity(Ah)','Discharge_Capacity(Ah)','Charge_Energy(Wh)','Discharge_Energy(Wh)','dV/dt(V/s)']]


#For S2
d4['Step_Index']=1
d5 = (df.loc[df['Step ID']==5]).copy()
d5 = df_copy.append(d5, ignore_index=True)
d5['Step_Index']=2
d5['Step_Time']=d5['Test_Time(s)']-d5['Test_Time(s)'][0]
d6 = (df.loc[df['Step ID']==6]).copy()
d6 = df_copy.append(d6, ignore_index=True)
d6['Step_Index']=3
d6['Step_Time']=d6['Test_Time(s)']-d6['Test_Time(s)'][0]
dr = d4.append([d5, d6], ignore_index=True)
dS2 = dr[['Test_Time(s)','Date_Time','Step_Time','Step_Index','Cycle_Index','Current(A)','Voltage(V)','Charge_Capacity(Ah)','Discharge_Capacity(Ah)','Charge_Energy(Wh)','Discharge_Energy(Wh)','dV/dt(V/s)']]


#For S3
d6['Step_Index']=1
d7 = (df.loc[df['Step ID']==7]).copy()
d7 = df_copy.append(d7, ignore_index=True)
d7['Step_Index']=2
d7['Step_Time']=d7['Test_Time(s)']-d7['Test_Time(s)'][0]
d8 = (df.loc[df['Step ID']==8]).copy()
d8 = df_copy.append(d8, ignore_index=True)
d8['Step_Index']=3
d8['Step_Time']=d8['Test_Time(s)']-d8['Test_Time(s)'][0]
dr = d6.append([d7, d8], ignore_index=True)
dS3 = dr[['Test_Time(s)','Date_Time','Step_Time','Step_Index','Cycle_Index','Current(A)','Voltage(V)','Charge_Capacity(Ah)','Discharge_Capacity(Ah)','Charge_Energy(Wh)','Discharge_Energy(Wh)','dV/dt(V/s)']]


#For S4
d8['Step_Index']=1
d9 = (df.loc[df['Step ID']==9]).copy()
d9 = df_copy.append(d9, ignore_index=True)
d9['Step_Index']=2
d9['Step_Time']=d9['Test_Time(s)']-d9['Test_Time(s)'][0]
d10 = (df.loc[df['Step ID']==10]).copy()
d10 = df_copy.append(d10, ignore_index=True)
d10['Step_Index']=3
d10['Step_Time']=d10['Test_Time(s)']-d10['Test_Time(s)'][0]
dr = d8.append([d9, d10], ignore_index=True)
dS4 = dr[['Test_Time(s)','Date_Time','Step_Time','Step_Index','Cycle_Index','Current(A)','Voltage(V)','Charge_Capacity(Ah)','Discharge_Capacity(Ah)','Charge_Energy(Wh)','Discharge_Energy(Wh)','dV/dt(V/s)']]

#Creating four different files for running ECM Algorithms
dS1.index = dS1.index+1
dS1.to_excel("./Script_data/" + File_Name[:-5] + "_S1.xlsx", sheet_name="S1", index_label="Data_Point")
dS2.index = dS2.index+1
dS2.to_excel("./Script_data/" + File_Name[:-5] + "_S2.xlsx", sheet_name="S2", index_label="Data_Point")
dS3.index = dS3.index+1
dS3.to_excel("./Script_data/" + File_Name[:-5] + "_S3.xlsx", sheet_name="S3", index_label="Data_Point")
dS4.index = dS4.index+1
dS4.to_excel("./Script_data/" + File_Name[:-5] + "_S4.xlsx", sheet_name="S4", index_label="Data_Point")