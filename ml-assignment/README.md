# Trigram Language Model

This repository contains the core assignment files for the **Trigram Language Model**.  
The model is trained on a text corpus and generates new text using trigram probabilities.

## How to Run

### Install Dependencies
Install the required Python package:
```bash
pip install pytest
```

### Generate Text
Run the model to generate sample text:
```bash
python src/generate.py
```
This will:  
- Load the corpus from `data/example_corpus.txt`  
- Train the trigram model  
- Generate a sample text of up to 50 words  

### Run Tests
To run the automated tests:
```bash
pytest
```

---

## Design Choices

All design decisions are documented in `evaluation.md`. The key points include:  
- **Text Cleaning Strategy:** How the input corpus is preprocessed  
- **Tokenization:** Splitting text into tokens for the trigram model  
- **Padding Tokens:** Use of `<s>` and `</s>` to denote sentence boundaries  
- **Data Structures:** Efficient structures for counting trigrams  
- **Probabilistic Sampling:** Method for generating text based on trigram probabilities  
- **Handling Unknown Words:** Approach for unseen words in the corpus  
- **Generation Logic:** How new text sequences are created  
- **Testing Approach:** How correctness of the model is verified

---

## Project Structure

```
Trigram-Language-Model/
│
├── data/
│   └── example_corpus.txt       # Sample corpus for training
│
├── src/
│   └── generate.py              # Script to train model and generate text
│
├── tests/
│   └── test_model.py            # Test cases for the model
│
├── evaluation.md                # Document explaining design choices
└── README.md                    # This file
