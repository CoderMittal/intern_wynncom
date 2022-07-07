# Cell Parameter Estimation
1. Use `Process_data` to parse the data into 3 different steps file namely S1, S2, S3.
    - Run `parser.py` script to generate step file in Folder named **Script_Data**
2. Use `dyn_model` to generate OCV-SOC Data for the Required Cell.
    - Run `data_visual.py` to plot the given Data for different Temperatures in the given Script.
    - Modify the paths and names according to your requirement and Data.
    - Run `dyn_model.py` to generate the cell Parameters for the given cell in my case **C6411**.
        - Some parameters are needed according to your requirements.
        1. Set variable `num_poles` for number of R-C Pairs required.
        2. Set variable `do_Hyst` to 1 if hystersis is required else set it to 0.
    - Above while generate the model for the above cell base on the selected variable.

# Observations and Results
## For No Hystersis
- ### Eta(Coulombic Efficiency Obtained)
    1. **T25** = 0.9998952724763747
    2. **T35** = 1.0267088333387768
    3. **T45** = 0.9942895225211908
- ### Q(Cell Capacity)
    1. **T25** = 5.250800039118811
    2. **T35** = 5.295335374554908
    3. **T45** = 5.329671778211747

# Modifications
- The cell capacity from our data was not a cumulative one so I had to add cell capacity at the end of each step.