import pandas as pd
import numpy as np

# Enter the file Name over Here
File_Name = './SW_ME_DYN_T45_1.xlsx'
Sheet = 'record'
############################
df = pd.read_excel(io=File_Name, sheet_name=Sheet)
df['time'] = df['Total Time'].str.split(':').apply(lambda x: int(x[0])*60*60 + int(x[1])*60 + int(x[2]))
df['time'] = (df['time']-df['time'][0])
df.rename(columns = {'Step ID':'step','Current(A)':'current','Chg Cap(Ah)':'chgAh', 'DChg Cap(Ah)':'disAh','Voltage(V)':'voltage'}, inplace = True)


# For S1
df_copy = df.iloc[:0,:].copy()
d2 = (df.loc[df['step']==2]).copy()
d2 = df_copy.append(d2, ignore_index=True)
d2['step']=1
# d2['time']=d2['time']-d2['time'][0]
d3 = (df.loc[df['step']==3]).copy()
d3 = df_copy.append(d3, ignore_index=True)
d3['step']=2
# d3['time']=d3['time']-d3['time'][0]
d4 = (df.loc[df['step']==4]).copy()
d4 = df_copy.append(d4, ignore_index=True)
d4['step']=3
# d4['time']=d4['time']-d4['time'][0]
d5 = (df.loc[df['step']==5]).copy()
d5 = df_copy.append(d5, ignore_index=True)
d5['step']=4
# d5['time']=d5['time']-d5['time'][0]
dr = d2.append([d3, d4, d5], ignore_index=True)
dS1 = dr[['time','step','current','voltage','chgAh','disAh']]


#For S2
d5['step']=1
d6 = (df.loc[df['step']==6]).copy()
d6 = df_copy.append(d6, ignore_index=True)
d6['step']=2
# d6['time']=d6['time']-d6['time'][0]
d7 = (df.loc[df['step']==7]).copy()
d7 = df_copy.append(d7, ignore_index=True)
d7['step']=3
# d7['time']=d7['time']-d7['time'][0]
dr = d5.append([d6, d7], ignore_index=True)
dS2 = dr[['time','step','current','voltage','chgAh','disAh']]


#For S3
d7['step']=1
d8 = (df.loc[df['step']==8]).copy()
d8 = df_copy.append(d8, ignore_index=True)
d8['step']=2
# d8['time']=d8['time']-d8['time'][0]
d9 = (df.loc[df['step']==9]).copy()
d9 = df_copy.append(d9, ignore_index=True)
d9['step']=3
# d9['time']=d9['time']-d9['time'][0]
dr = d7.append([d8, d9], ignore_index=True)
dS3 = dr[['time','step','current','voltage','chgAh','disAh']]

dS1.to_csv("./Script_data/" + File_Name[:-5] + "_S1.csv", index=False)
dS2.to_csv("./Script_data/" + File_Name[:-5] + "_S2.csv", index=False)
dS3.to_csv("./Script_data/" + File_Name[:-5] + "_S3.csv", index=False)