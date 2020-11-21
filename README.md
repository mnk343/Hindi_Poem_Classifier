# Hindi Poem Classifier

Poetry analysis in Indic languages has not received as much attention in recent years and this project is motivated towards starting that endeavour. Also the challenge that the level of ambiguity and subtlety that this problem provides provided a big motivation for us to tackle.

Our project: **Heritage - The Poem Classifier** employs various methods and models taught in the course CS565 Intelligent Systems and Interfaces to correctly predict the eras and author names of a given input poem.

## Workflow
The workflow of the project is as follows and can be found in various different files of the project:

- **Data Collection**
    - Used **Scrapy** and **Beautiful Soup** to parse different websites to build a corpus of **50,000+** poems
    - The scraped poems were then merged after removing repeated poems.
 - **Pre-processing**
    - Used libraries such as **iNLTK** to attempt pre-precessing of the poems and then removed the stop words. 
  - **Vectorization**
    - Employed various different types of vectorization methods to get the corresponding word  embeddings.
    - Used pre-built vectorization libraries to for **BTF** (Binary Term Frequency), **BoW** (Bag of Words), **TFL1** (Term Frequency with L1 normalization) and **TF-IDF** (Full Term Frequency Inverse Document Frequency)
    - Implemented **GloVe** model from scratch to find the word vector embeddings and used them to get document vectors.
- **Model Training and Classification**
    - Testing of different models was done on this step.
    - Employed Natural Language Processing models like cosine similarity to find the closest poem a given input matches and predicted the era and author based on that.
    - Also used machine learning models like **Logistic Regression** for predictions.
    - Also used Deep Learning based models like **CNN** and **LSTM** and compared the results among all the different models.


## Installation and Usage
#### Crawler
Install the dependencies.
```sh
$ pip install Scrapy
```
Run the crawler:
```sh
$  cd Dataset\ Creation\(Crawler\ +\ Dataset\ Creation\)/crawler_Scrapy/
$ scrapy crawl poems
```

#### Pre-Processing and Model Training

Install the dependencies.
```sh
$ pip install inltk
```
Run the necessary files:
```sh
$  cd  directory_name/
$ python3 *.py
```
#### Results
We got the following results:
For **Era** prediction:
![Era Prediction Graph](https://github.com/mnk343/Hindi_Poem_Classifier/blob/main/Project_Reports/Images/era_prediction_results.png?raw=true)

For **Author** prediction:
![Author Prediction Graph](https://github.com/mnk343/Hindi_Poem_Classifier/blob/main/Project_Reports/Images/poet_prediction_results.png?raw=true)


#### Final Remarks
In this work, we compare different approaches for determining era and poets of Hindi poems.
The vectorization was done using 5 methods, namely Binary Term Frequency, Bag of Words, (L1) Normalised Term Frequency ,(L2) Normalised TF-IDF and GloVe (used as word embeddings in LSTM model and used to calculate document vectors for other models). The models used were Cosine Similarity, Logistic Regression, Convolution Neural Networks, and Long Short Term Memory.
This work also serves the evaluation of poems whose sources are not known. CNN models perform better than cosine similarity and logisitic regression based models on the dataset considered.
This project explores new dimensions by improving the quality of Poem Classification for Hindi Language and hopes to generate more effort in this domain.










