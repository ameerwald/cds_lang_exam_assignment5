# import packages - basics 
import pandas as pd
import os
import numpy as np
# to import the fine tuned model 
from transformers import pipeline
# for visualizations 
from matplotlib import pyplot as plt
import seaborn as sns
# to be able to use utils from the folder 
import sys
sys.path.append("utils")
from langutils import load_data
from langutils import classify
from langutils import plot_by_year
from langutils import plot_years
from langutils import visualize_emotions




def main():
    # load the data
    data, headlines, category, year, df  = load_data()
    # loads model, classifies headlines, and makes df 
    classifier, emotion, df = classify(headlines, year)
    # make bar plot for each year and save it 
    years, year_dataframes, sorted_year_dataframes = plot_by_year(df)
    # compile all the year plots in one and make it pretty 
    plot_years(year, df, year_dataframes)
    # one bar plot of emotions overall samples headlines and save it 
    visualize_emotions(df)




if __name__=="__main__":
    main()