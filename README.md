
# Assignment 5 - Using finetuned transformers via HuggingFace for headline emotion classification

## Github repo link

This assignment can be found at my github [repo](https://github.com/ameerwald/cds_lang_exam_assignment5).

## The data

This dataset is a collection of news headlines all from HuffPost between 2012-2022. The dataset can be found [here](https://www.kaggle.com/datasets/rmisra/news-category-dataset).


## Assignment description

For this assignment, I used ```HuggingFace``` in a similar way to the previous assignment. Therefore I did the following:

- Initialize a ```HuggingFace``` pipeline for emotion classification
- Perform emotion classification for political headlines in the data
- Assuming the most likely prediction is the correct label, create visualisations which show the following:
  - Distribution of emotions across all of the data
- Comparing the results, looking at emotion classification over the whole dataset and over the years. 



# Repository 

| Folder         | Description          
| ------------- |:-------------:
| In      | This folder is hidden due to the size of the dataset
| Notes | Jupyter notebook and script with notes       
| Out  | Visual representations of the data   
| Src  | Py script 
| Utils  |        


## To run the scripts 

As the dataset is too large to store in my repo, use the link above to access the data. Download and unzip the data. Then create a folder called  ```in``` within the assignment 5 folder, along with the other folders in the repo. Then the code will run without making any changes. If the data is placed elsewhere, then the path should be updated in the code.

1. Clone the repository, either on ucloud or something like worker2
2. From the command line, at the /cds_lang_exam_assignment5/ folder level, run the following lines of code. 

This will create a virtual environment, install the correct requirements.
``` 
bash setup.sh
```
While this will run the scripts and deactivate the virtual environment when it is done. 
```
bash run.sh
```

This has been tested on an ubuntu system on ucloud and therefore could have issues when run another way.

# Discussion of results 

When looking at the emotions overall of the political headlines from HuffPost from 2012-2022, neutral is by far the most common emotion. Following thing appears to be sadness followed closely with joy and fear.


It is possible to select a year and look at those emotions alone or look at all bar graphs over the years together. In that view, it is easier to see how the emotions have varied over time, that is of course assuming the classification is accurate which we are for the sake of this assignment. Anger and disgust appear to have increased over the years, not every single year but it appears to be an overall trend. Joy appears to fluctuate, staying the same over many years then going down in 2021 and then up in 2022. Surprise also stays the same awhile and then fluctuates both up and down in recent years. Another important factor is that there are not the same amount of headlines in each year. When looking at the y-axis of the graphs they vary quite drastically.


Overall it was interesting to see the emotions of political headlines over the years. I expected some more drastic changes in 2016 when Trump took office although it does appear that anger and fear increased in that time which would align with a left leaning source like HuffPost. I also thought 2020 would show some differences from COVID but it appears that fear and anger were higher in 2019.





