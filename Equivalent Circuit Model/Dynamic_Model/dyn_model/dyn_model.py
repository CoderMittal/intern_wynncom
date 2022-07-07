"""
Dyn model
"""

import numpy as np
import json

from funcs import processDynamic
from models import DataModel, ModelOcv

from pathlib import Path

# parameters
cellID = 'C6411'     # cell identifier
numpoles = 2        # number of resistor-capacitor pairs in final model
temps = [25, 35, 45]   # temperatures
doHyst = 0          # 1 "find M, M0 and G params" or 0 "make hys params 0" 

# read model OCV file, previously computed by runProcessOCV
modelocv = ModelOcv.load(Path(f'../../OCV Static/{cellID}.json'))

# initialize array to store battery cell data
data = np.zeros(len(temps), dtype=object)

# load battery cell data for each temperature as objects then store in data array
# note that data files are in the dyn_data folder
print('Load files')
for idx, temp in enumerate(temps):
    # mag = mags[idx]
    if temp < 0:
        tempfmt = f'{abs(temp):02}'
        files = [Path(f'../Process_data/Script_data/SW_ME_DYN_T{tempfmt}_1_S1.csv'),
                 Path(f'../Process_data/Script_data/SW_ME_DYN_T{tempfmt}_1_S2.csv'),
                 Path(f'../Process_data/Script_data/SW_ME_DYN_T{tempfmt}_1_S3.csv')]
        data[idx] = DataModel(temp, files)
        print(*files, sep='\n')
    else:
        tempfmt = f'{abs(temp):02}'
        files = [Path(f'../Process_data/Script_data/SW_ME_DYN_T{tempfmt}_1_S1.csv'),
                 Path(f'../Process_data/Script_data/SW_ME_DYN_T{tempfmt}_1_S2.csv'),
                 Path(f'../Process_data/Script_data/SW_ME_DYN_T{tempfmt}_1_S3.csv')]
        data[idx] = DataModel(temp, files)
        print(*files, sep='\n')

modeldyn = processDynamic(data, modelocv, numpoles, doHyst)

# convert ocv and dyn results model object to dict, then save in JSON to disk 
modeldyn = {k:v.tolist() if isinstance(v, np.ndarray) else v for k,v in modeldyn.__dict__.items()}
if True:
    if doHyst:
        with open(f'../modeldyn-{cellID}.json', 'w') as json_file:
            json.dump(modeldyn, json_file, indent=4)
    else:
        with open(f'../modeldyn-no-hys-{cellID}.json', 'w') as json_file:
            json.dump(modeldyn,json_file, indent=4)