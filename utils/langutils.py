# import packages - basics 
import pandas as pd
import os
import numpy as np
# to import the fine tuned model 
from transformers import pipeline
# for visualizations 
from matplotlib import pyplot as plt
import seaborn as sns

def load_data():
    # load in the data
    filename = os.path.join("in", "News_Category_Dataset_v3.json")
    data = pd.read_json(filename, lines=True)
    # narrowing category to political headlines 
    category = data.loc[data['category'] == 'POLITICS']
    # taking a random sample of 20,000 headlines in the politics category 
    df = data.sample(n=20000)
    # turning the headlines into a list of strings 
    headlines = df['headline'].astype(str).values.tolist()
    # turning the date column into just the year 
    year = df['date'].dt.strftime('%Y')
    return data, headlines, category, year, df 


def classify(headlines, year):
    # giving updates
    print("Loading model...")
    # load in the model used for classification from hugging face 
    classifier = pipeline("text-classification", 
                        model="j-hartmann/emotion-english-distilroberta-base", 
                        return_all_scores=False)
    # print this because it takes about 30 min to classify the headlines 
    print("Classifying headlines...")
    # running the classifier on the headlines 
    emotion = classifier(headlines)
    # make dataframe with headlines, labels and top emotion
    df = pd.DataFrame(list(zip(headlines, year, emotion)), columns=['title', 'year', 'emotion'])
    df['emotion'] = df['emotion'].apply(lambda x: x['label'])
    # set categorical order for plotting later 
    df['emotion'] = pd.Categorical(df['emotion'],
                                    categories=['anger', 'disgust', 'fear', 'joy', 'neutral', 'sadness', 'surprise'],
                                    ordered=True)
    return classifier, emotion, df


def plot_by_year(df):
    # getting each year 
    years = df['year'].unique()
    # making a dictionary to store separate dataframes for each year
    year_dataframes = {}
    for year in years:
        year_dataframes[year] = df[df['year'] == year].copy()
    # putting the year dfs in order 
    sorted_year_dataframes = sorted(year_dataframes.items(), key=lambda x: x[0])
    # plotting count bar plots for each year and saving them  
    for year, year_df in sorted_year_dataframes:
        plt.figure(figsize=(8, 6)) 
        
        sns.countplot(x='emotion', data=year_df)
        plt.title(f'Emotion Distribution for Year {year}')
        plt.xlabel('Emotion')
        plt.ylabel('Count')
        plt.savefig(f'out/bar_plot_{year}.png')
        plt.show()
    return years, year_dataframes, sorted_year_dataframes
    


def plot_years(year, df, year_dataframes):
    # make dataframes for each year using a for loop
    for year in range(2012, 2023):
        df_name = f"df_{year}"
        df_year = year_dataframes.get(str(year), pd.DataFrame())
        globals()[df_name] = df_year
    # create a list of the separate year dfs 
    dataframes = [df_2012, df_2013, df_2014, df_2015, df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022]
    # define the emotions color palette
    palette = ['#DDF1FF', '#AADDFF', '#88D0FF', '#56bdff','#3C84B2', '#2B5E7F', '#19384C']
    # create a figure and axes for the subplots
    fig, axes = plt.subplots(4, 3, figsize=(20, 20))
    axes = axes.flatten()
    # iterate over the dataframes and axes together
    for df, ax, year in zip(dataframes, axes, range(2012, 2023)):
        # make count plot for each dataframe and assign it to the corresponding axis
        sns.countplot(x=df['emotion'], palette=palette, ax=ax).set(
            title=f"Emotions in {year} headlines", xlabel=None)
    # adjust the layout and spacing
    plt.tight_layout()
    plt.savefig('out/bar_plot_ALL.png')
    # clear the figure so it saves correctly
    plt.clf() 


def visualize_emotions(df):
    # create a figure and axes for the emotions plot
    fig, ax = plt.subplots(figsize=(10, 6))
    # plotting emotions overall, not separated by year 
    sns.countplot(x=df['emotion'], ax=ax)
    plt.savefig('out/emotions_for_ALL_headlines.png')
    plt.clf() 