# OCV Generation
1. Use `process_data` to parse the data into 4 different steps file namely S1, S2, S3, S4.
    - Run `parser.py` script to generate step file in Folder named **Script_Data**
2. Use `model_OCV` to generate OCV-SOC Data for the Required Cell.
    - Run `data_visual.py` to plot the given Data for different Temperatures in the given Script.
    - Modify the paths and names according to your requirement and Data.
    - Run `ocv.py` to plot the OCV-SOC curve and generate data as JSON file in my case is `C6411.json`.


# Observations and Results
- ### Eta(Coulombic Efficiency Obtained)
    1. **T25** = 1.0018142414155637
    2. **T35** = 1.0010345112736965
    3. **T45** = 1.000862950451423
- ### Q(Cell Capacity)
    1. **T25** = 5.27898
    2. **T35** = 5.41974
    3. **T45** = 5.43035

# Modifications
- The cell capacity from our data was not a cumulative one so I had to add cell capacity at the end of each step.