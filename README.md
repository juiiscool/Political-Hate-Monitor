# Political Hate Speech Monitor

## NLP-Based Analysis Tool for Albanian Political Comments

Political Hate Speech Monitor is a web-based NLP project developed to explore potentially toxic language in a corpus of Albanian political comments.

The application allows users to search for a specific word or phrase and analyze the comments in which that term appears. It displays the matching cleaned comments together with hate speech and sentiment information, and calculates a toxicity score for the selected search term.

> **Important:** The toxicity score represents the characteristics of the comments containing the searched term. It does not classify the word itself as inherently toxic.

---

## Features

- Search for words or phrases in Albanian political comments
- Display cleaned comments containing the searched term
- Count matching comments
- Identify comments labeled as hate speech
- Identify comments labeled with negative sentiment
- Calculate a toxicity score
- Categorize toxicity to:
  - LOW
  - MEDIUM
  - HIGH
- Display results through a simple web interface
- Process the dataset using Python and Pandas
- Run the application locally using Flask

---

## Project Structure

```text
political_hate_monitor/
│
├── dataset/
│   └── comments.xlsx
│
├── templates/
│   └── index.html
│
├── venv/
│
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
