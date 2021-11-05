# Deploy
+ Doing `notebook_midproject.ipynb` and create pickle file `rf.pkl` on Kaggle
+ Creating `app1.py` on `VSC` with `streamlit as st`
+ Creating `requirements.txt` with `pipreqs` from `Anaconda Prompt`
+ Deploy app from existing repo on `Github` with `Streamlit Cloud`  

### Click! [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/irfanim/ml_zoomcamp/main/app1.py)

# Problem description
## Heart Failure Prediction - 12 clinical features for predicting death events.

> Cardiovascular diseases (CVDs) are the number 1 cause of death globally, taking an estimated 17.9 million lives each year, 
which accounts for 31% of all deaths worlwide.

> Heart failure is a common event caused by CVDs and this dataset contains 12 features that can be used to predict mortality by heart failure.

> Most cardiovascular diseases can be prevented by addressing behavioural risk factors such as tobacco use, 
unhealthy diet and obesity, physical inactivity and harmful use of alcohol using population-wide strategies.

> People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help.

## Features
    
    
+ ### age
> Age of patient, between 40 years old until 95 years old 
+ ### anaemia
Decrease of red blood cells or hemoglobin (boolean) - 0 = No, 1 = Yes
+ ### creatinine_phosphokinase
> Level of the CPK enzyme in the blood (mcg/L)
+ ### diabetes
> If the patient has diabetes (boolean) - 0 = No, 1 = Yes
+ ### ejection_fraction
> Percentage of blood leaving the heart at each contraction (percentage)
+ ### high_blood_pressure
> If the patient has hypertension (boolean) - 0 = No, 1 = Yes
+ ### platelets
> Platelets in the blood (kiloplatelets/mL)
+ ### serum_creatinine
> Level of serum creatinine in the blood (mg/dL)
+ ### serum_sodium
> Level of serum sodium in the blood (mEq/L)
+ ### sex
> Woman or man (binary) - Female = 0, Male = 1
+ ### smoking
0 = No, 1 = Yes
+ ### time
> not enough information, between 4 until 285


## TARGET
+ ### DEATH_EVENT
> 0 = No, 1 = Yes






# Reff:

+ https://www.kaggle.com/andrewmvd/heart-failure-clinical-data

# Acknowledgements:
+ Citation

> Davide Chicco, Giuseppe Jurman: Machine learning can predict survival of patients with heart failure from serum creatinine and ejection fraction alone. BMC Medical Informatics and Decision Making 20, 16 (2020). (https://doi.org/10.1186/s12911-020-1023-5)
License CC BY 4.0
