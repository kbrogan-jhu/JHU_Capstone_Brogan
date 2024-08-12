#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:23:19 2024

@author: kevinbrogan
"""
import os
import requests
import pandas as pd

# Set the working directory
os.chdir('/Users/kevinbrogan/Desktop/HopkinsCapstone/PythonScripts/')

# years included in analysis (2013-2023)
years = [str(year) for year in range(2013, 2024)]


sbir_data = pd.DataFrame()

# Run loop to query sbir.gov API
for year in years:
    base_url = "https://www.sbir.gov/api/awards.json?"
    yr = f"year={year}"
    row_parameter = "&rows=10000"
    
    final_url = f"{base_url}{yr}{row_parameter}"
    
    response = requests.get(final_url)
    data = response.json()
    
   
    sbir_data = pd.concat([sbir_data, pd.json_normalize(data)])

# Write to csv
sbir_data.to_csv("sbirsttrData_2013_2023.csv", index=False)
