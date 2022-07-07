# ECM_Yash
ESCtoolbox python implementation with sinowatt cell data
### OCV-SOC Generation
1. Generated Parsed data for different steps in accordance with **ECM-python** in `process_data` directory.
2. Plotted the given data for different Temperature and made observations using `data_visual.py` .
3. Created JSON file containing the OCV-SOV data and Plotted the SOC Curves.The RMS-error in the predicted result was to be noted in range of 0.1-0.2 mv.

### Cell Parameters Estimation
1. Parsed the Data for various Steps in `process_data` directory.
2. Used Data from OCV-SOC curve from OCV Static and the above parsed Data to estimate the Cell Parameters for **C6411**.

### *Note-* The following code is inspired from *Gregory Plett's-* `esctoolbox` and it is modified according to our data.