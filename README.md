# NLP Project: Text Analysis and Sentiment Detection
> This project showcases a comprehensive Natural Language Processing (NLP) workflow, encompassing text similarity analysis, spam detection, topic modeling, sentiment analysis, web scraping, and transformer-based applications, utilizing a diverse array of libraries and techniques to tackle various NLP tasks.

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Repository Contents](#repository-contents)
3. [Key Features & Analysis](#key-features--analysis)
4. [Datasets](#datasets)
5. [Methodology](#methodology)
6. [Tech Stack](#tech-stack)
7. [Installation](#installation)
8. [How to Run](#how-to-run)
9. [Results & Outputs](#results--outputs)
10. [Contributing](#contributing)
11. [License](#license)

## 📖 Project Overview
This NLP project tackles a variety of text analysis tasks, including the similarity between texts, spam detection in messages, topic modeling in documents, sentiment analysis of tweets, web scraping for data extraction, and leveraging transformers for advanced language understanding. The goal is to demonstrate a thorough understanding of NLP concepts and their practical applications using Python libraries such as NLTK, SpaCy, scikit-learn, and transformers.

## 📁 Repository Contents
The repository contains the following notebooks and files:
- `Similarity of Texts.ipynb`: This notebook explores the similarity between words and sentences using Wordnet from NLTK and SpaCy's language models.
- `Spam-Ham Detection.ipynb`: Focuses on detecting spam messages, utilizing a dataset of labeled messages to train and evaluate a spam detector based on TF-IDF features and a Naive Bayes classifier.
- `TDM_TFIDF.ipynb`: Deals with Term Document Matrix (TDM) creation and Term Frequency-Inverse Document Frequency (TF-IDF) transformation to analyze document similarity and keyword extraction.
- `Twitter Sentimient Analysis.ipynb`: Analyzes the sentiment of tweets using NLTK's VADER, TextBlob, and transformer-based models for sentiment classification and intensity prediction.
- `Web Scrapping.ipynb`: Demonstrates how to scrape data from websites using BeautifulSoup and request libraries, including extracting specific data points like page titles.
- `tpicmodeling.ipynb`: Applies topic modeling techniques, such as Latent Dirichlet Allocation (LDA), to a corpus of documents to uncover underlying topics and trends.
- `transformers.ipynb`: Explores the capabilities of transformer models, including text summarization, question answering, and language translation using the Hugging Face Transformers library.
- `wordcloud.ipynb`:Though not fully examined due to its size, this notebook is intended for generating word clouds from text data, visually representing the frequency of words.

## ✨ Key Features & Analysis
1. **Word Similarity**: The project calculates the similarity between words using Wordnet, allowing for the understanding of semantic relationships.
2. **Spam Detection**: It employs a supervised learning approach to detect spam messages, leveraging TF-IDF vectorization and a Multinomial Naive Bayes classifier.
3. **Term Document Matrix**: The creation of TDMs and TF-IDF transformations enable the analysis of document collections for similarity and keyword extraction.
4. **Sentiment Analysis**: Sentiment of tweets is analyzed using multiple approaches, including rule-based models (VADER) and machine learning models (TextBlob and transformers), providing a comprehensive view of sentiment intensity and classification.
5. **Web Scraping**: The project demonstrates how to extract data from web pages, including how to handle HTML parsing and how to simulate user requests.
6. **Topic Modeling**: LDA is applied to uncover topics in a set of documents, helping in understanding the thematic structure of the corpus.

## 🗂️ Datasets
- The `spam.csv` dataset contains labeled messages (spam/ham) used for training and testing the spam detector.
- The `Tweets.csv` dataset includes tweets used for sentiment analysis, containing text and corresponding sentiment labels.
- Other notebooks may use smaller, example datasets or generated text for demonstration purposes.

## 🧠 Methodology
1. **Data Preparation**: Each notebook begins with data loading and preprocessing steps, which include text cleaning, normalization, and feature extraction as necessary.
2. **Model Selection and Training**: Depending on the task, the project selects appropriate models (e.g., Naive Bayes for spam detection, LDA for topic modeling) and trains them on prepared datasets.
3. **Model Evaluation**: Trained models are evaluated on test sets or using cross-validation to assess their performance and generalizability.
4. **Analysis and Visualization**: Results are analyzed, and insights are visualized through word clouds, topic distributions, or sentiment scores to facilitate understanding.

## 🛠️ Tech Stack
- **NLTK**: For natural language processing tasks, including tokenization, stemming, and corpora manipulation.
- **SpaCy**: Utilized for high-performance, streamlined processing of text data, including entity recognition and language models.
- **scikit-learn**: Provides a wide range of machine learning algorithms, including those for classification, clustering, and topic modeling.
- **Transformers**: The Hugging Face transformers library is used for advanced language models and tasks like text summarization and question answering.
- **BeautifulSoup and requests**: For web scraping tasks, handling HTML parsing and HTTP requests.

## ⚙️ Installation
To replicate this project, install the required libraries by running:
```bash
pip install nltk spacy scikit-learn transformers requests beautifulsoup4
```
Additionally, ensure you download necessary NLTK data using:
```python
import nltk
nltk.download('wordnet')
nltk.download('stopwords')
```
And install specific SpaCy models:
```python
python -m spacy download en_core_web_md
```

## 🚀 How to Run
1. Clone the repository: `git clone https://github.com/shrvni2/nlp.git`
2. Install required libraries as instructed above.
3. Open each notebook in an environment where the necessary libraries are installed (e.g., Jupyter Notebook).
4. Run each cell in sequence to execute the analysis and view the results.

## 📊 Results & Outputs
Results from each notebook will provide insights into the specific NLP tasks, such as spam messages identified, sentiment scores for tweets, topics extracted from documents, and summaries of input texts. These outputs can be used for further analysis or as inputs for other NLP tasks.

## 🤝 Contributing
Contributions are welcome in the form of new notebooks or enhancements to existing ones, covering more NLP tasks or utilizing different libraries and models. Please fork the repository, make your changes, and submit a pull request.

## 📄 License
This project is licensed under the MIT License, allowing for free use, modification, and distribution. See LICENSE for details.