# ITNPA34_-Project-2
# Research Document Mining and Classification

## Project Overview

This project focuses on analysing research abstracts and research documents using machine learning and natural language processing techniques.

The project has two main parts. The first part classifies research abstracts as either **AI-related research** or **classical research**. The second part applies document mining techniques to a collection of research articles to identify important information, summarise documents and discover topics.

The project was developed using Python and Jupyter Notebook, with a Streamlit web application created for testing the final research abstract classifier.

## Project Objectives

The main objectives of the project were to:

- Prepare and clean research abstract data.
- Train and compare different machine learning classification models.
- Improve the performance of the selected model using hyperparameter tuning.
- Deploy the final classifier using Streamlit.
- Create a dataframe containing research articles and their content.
- Preprocess the research article text.
- Summarise research articles using text summarisation techniques.
- Identify topics across the research documents using LDA.
- Visualise the identified topics.
- Create a GitHub repository containing the project documentation, datasets, notebooks and deployment files.

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Matplotlib
- WordCloud
- Joblib
- Streamlit
- pyLDAvis

## Project Structure

```text
Research-Document-Mining/
│
├── README.md
│
├── datasets/
│   ├── research_abstracts.json
│   ├── research_1.txt
│   ├── research_2.txt
│   ├── research_3.txt
│   ├── research_4.txt
│   └── research_5.txt
│
├── notebooks/
│   └── Research_Document_Mining.ipynb
│
└── deployment/
    ├── app.py
    ├── research_abstract_classifier.pkl
    └── README.md
```

## Project Questions

### Question 1

The first stage focuses on preparing the research abstract dataset and establishing a baseline classification model.

The abstracts are converted into numerical features using TF-IDF before being used for machine learning.

### Question 2

Four machine learning models were trained and compared:

- Random Forest
- Linear SVM
- Multinomial Naive Bayes
- Logistic Regression

Random Forest produced the strongest overall results and was selected for further tuning.

GridSearchCV was then used to improve the Random Forest configuration.

The final tuned model achieved:

- **Accuracy:** 92.44%
- **Macro F1-score:** 0.8668
- **AI recall:** 63.83%

The final model was saved as:

```text
research_abstract_classifier.pkl
```

### Question 2.3 – Web Interface

A Streamlit application was developed to allow users to enter a research abstract and receive a prediction.

The application classifies the abstract as either:

- AI Research
- Classical Research

The application code is available in:

```text
deployment/app.py
```

### Question 3

The document mining section uses five research articles stored as text files.

The articles are loaded into a dataframe and processed using text preprocessing techniques. The cleaned content is then used for summarisation and topic analysis.

The following techniques were used:

- Text cleaning
- Stop-word removal
- TF-IDF-based extractive summarisation
- Word-cloud visualisation
- Latent Dirichlet Allocation (LDA)
- Topic distribution analysis

### Question 4

LDA was used to identify topics within the research documents. The most important words for each topic were extracted and visualised.

An interactive topic visualisation was also created using pyLDAvis. This allows the topics and their most salient words to be explored interactively.

## Dataset

The project uses:

### Research Abstract Dataset

`research_abstracts.json`

This dataset contains research abstracts and their associated classification labels.

### Research Article Dataset

Five research documents are included:

```text
research_1.txt
research_2.txt
research_3.txt
research_4.txt
research_5.txt
```

These documents are used for the document mining, summarisation and topic modelling sections.

## How to Run the Notebook

1. Clone or download this repository.
2. Open the `notebooks` folder.
3. Open `Research_Document_Mining.ipynb` using Jupyter Notebook or JupyterLab.
4. Make sure the required Python packages are installed.
5. Run the notebook cells in order.

## How to Run the Streamlit Application

Open a terminal and navigate to the deployment folder:

```bash
cd deployment
```

Then run:

```bash
streamlit run app.py
```

The application will open in a web browser.

Make sure the following files are in the same deployment folder:

```text
app.py
research_abstract_classifier.pkl
```

## Results

The machine learning models produced different classification results. Random Forest performed best overall among the models tested.

After hyperparameter tuning, the final Random Forest classifier achieved an accuracy of **92.44%** and a macro F1-score of **0.8668**.

The document mining section also showed that research articles could be processed and analysed to identify common themes using LDA.

## Repository Contents

This repository contains:

- Project documentation
- Research datasets
- Jupyter Notebook
- Machine learning model
- Streamlit application
- Deployment instructions

The repository is intended to provide the complete workflow from data preparation and model development through to document mining and deployment.
