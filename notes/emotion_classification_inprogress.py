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
    filename = os.path.join("..", "in", "News_Category_Dataset_v3.json")
    data = pd.read_json(filename, lines=True)
    # turning the headlines into a list of strings 
    headlines = data['headline'].astype(str).values.tolist()
    # narrowing category to political headlines 
    category = data.loc[data['category'] == 'POLITICS']
    # turning the date column into just the year 
    year = more_df['date'].dt.strftime('%Y')
    # Create DataFrame with headlines, category labels, and the year 
    df = pd.DataFrame(list(zip(headlines, category, year)), columns=['headlines', 'category', 'year'])
    # Narrowing down to 10,000 headlines 
    df = df.sample(n=10000)
    return data, headlines, category, year, df 


def classify(headlines):
    # load in the model used for classification from hugging face 
    classifier = pipeline("text-classification", 
                        model="j-hartmann/emotion-english-distilroberta-base", 
                        return_all_scores=False) # giving only the highest emotion 
    # running the classifier on the headlines 
    emotion = classifier(headlines)
    return classifier, emotion

def emotion_score(headlines, emotion, year):
    # creating empty lists to append the scores to for each emotion 
    anger = []
    disgust = []
    fear = []
    joy = []
    neutral = []
    sadness = []
    surprise = []
    # extract scores 
    for i in range(len(headlines)):
        anger.append(emotion[i][0].get("score"))
        disgust.append(emotion[i][1].get("score"))
        fear.append(emotion[i][2].get("score"))
        joy.append(emotion[i][3].get("score"))
        neutral.append(emotion[i][4].get("score"))
        sadness.append(emotion[i][5].get("score"))
        surprise.append(emotion[i][6].get("score"))
    # Create DataFrame with headlines, year and all the emotions 
    df = pd.DataFrame(list(zip(headlines, year, anger, disgust, fear, joy, neutral, sadness, surprise)), columns=['headlines', 'year', 'anger', 'disgust', 'fear', 'joy', 'neutral', 'sadness', 'surprise'])
    # find the top emotion
    df['top_emotion'] = df[['anger', 'disgust', 'fear', 'joy', 'neutral', 'sadness', 'surprise']].idxmax(axis=1)
    return df

def year_filter():
    # filter into their own dfs by year 
    df_2017 = df[ (df['year'] == '2017') ]
    df_2018 = df[ (df['year'] == '2018') ]
    df_2019 = df[ (df['year'] == '2019') ]
    df_2020 = df[ (df['year'] == '2020') ]
    df_2021 = df[ (df['year'] == '2021') ]
    df_2022 = df[ (df['year'] == '2022') ]

def plot_all(df_2017, df_2018, df_2019, df_2020, df_2021, df_2022):
    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3,2, figsize=(30, 12))
    ax1 = sns.countplot(x=df_2017['emotion'], palette = ['#DDF1FF', '#AADDFF', '#88D0FF', '#56bdff','#3C84B2', '#2B5E7F', '#19384C'], ax=ax1).set(
        title="Emotions in 2017 headlines", xlabel=None)
    ax2 = sns.countplot(x=df_2018['emotion'], palette = ['#DDF1FF', '#AADDFF', '#88D0FF', '#56bdff','#3C84B2', '#2B5E7F', '#19384C'], ax=ax2).set(
        title="Emotions in 2018 headlines", xlabel=None)
    ax3 = sns.countplot(x=df_2019['emotion'], palette = ['#DDF1FF', '#AADDFF', '#88D0FF', '#56bdff','#3C84B2', '#2B5E7F', '#19384C'], ax=ax3).set(
        title="Emotions in 2019 headlines", xlabel=None)
    ax4 = sns.countplot(x=df_2020['emotion'], palette = ['#DDF1FF', '#AADDFF', '#88D0FF', '#56bdff','#3C84B2', '#2B5E7F', '#19384C'], ax=ax4).set(
        title="Emotions in 2020 headlines", xlabel=None)
    ax5 = sns.countplot(x=df_2021['emotion'], palette = ['#DDF1FF', '#AADDFF', '#88D0FF', '#56bdff','#3C84B2', '#2B5E7F', '#19384C'], ax=ax5).set(
        title="Emotions in 2021 headlines")
    ax6 = sns.countplot(x=df_2022['emotion'], palette = ['#DDF1FF', '#AADDFF', '#88D0FF', '#56bdff','#3C84B2', '#2B5E7F', '#19384C'], ax=ax6).set(
        title="Emotions in 2022 headlines")
    plt.show()

def visualize(df):
    # plotting top emotions over all years, then for each 
    sns.countplot(x=df['top_emotion'])
    plt.savefig('out/emotions_for_ALL_headlines.png')
    df_2017 = df[df['year'] == '2017']
    sns.countplot(x=df_2017['top_emotion'])
    plt.savefig('out/emotions_for_2017_headlines.png')
    df_2018 = df[df['year'] == '2018']
    sns.countplot(x=df_real['top_emotion'])
    plt.savefig('out/emotions_for_2018_headlines.png')
    df_2019 = df[df['year'] == '2019']
    sns.countplot(x=df_2017['top_emotion'])
    plt.savefig('out/emotions_for_2019_headlines.png')
    df_2020 = df[df['year'] == '2020']
    sns.countplot(x=df_real['top_emotion'])
    plt.savefig('out/emotions_for_2020_headlines.png')
    df_2021 = df[df['year'] == '2021']
    sns.countplot(x=df_2017['top_emotion'])
    plt.savefig('out/emotions_for_2021_headlines.png')
    df_2022 = df[df['year'] == '2022']
    sns.countplot(x=df_real['top_emotion'])
    plt.savefig('out/emotions_for_2022_headlines.png')
    return df_2017, df_2018, df_2019, df_2020, df_2021, df_2022


dfs = [df_2017, df_2018, df_2019, df_2020, df_2021, df_2022]
for i in dfs:
    df.apply(pd.Series.value_counts)
# for tables
emotions_2017 = df_2017['emotion'].value_counts()[0:7]
emotions_2018 = df_2018['emotion'].value_counts()[0:7]
emotions_2019 = df_2019['emotion'].value_counts()[0:7]
emotions_2020 = df_2020['emotion'].value_counts()[0:7]
emotions_2021 = df_2021['emotion'].value_counts()[0:7]
emotions_2022 = df_2022['emotion'].value_counts()[0:7]
# save the report 
with open(os.path.join("out", "emotions_report_2017.txt"), "w") as f:
    f.write(emotions_2017))
with open(os.path.join("out", "emotions_report_2018.txt"), "w") as f:
    f.write(emotions_2018))
with open(os.path.join("out", "emotions_report_2019.txt"), "w") as f:
    f.write(emotions_2019))
with open(os.path.join("out", "emotions_report_2020.txt"), "w") as f:
    f.write(emotions_2020))
with open(os.path.join("out", "emotions_report_2021.txt"), "w") as f:
    f.write(emotions_2021))
with open(os.path.join("out", "emotions_report_2022.txt"), "w") as f:
    f.write(emotions_2022))



def main():
    # load the data
    filename, data, headlines, label = load_data()
    # create the classifer 
    classifer, emotion = classify(headlines)
    # label headlines as the top emotion 
    df = emotion_score(headlines, emotion, label)
    visualize(df)



if __name__=="__main__":
    main()