## Trigram Language Model

This directory contains the core assignment files for the Trigram Language Model.
The model is trained on a text corpus and generates new text using trigram probabilities.

## How to Run 

    **Install pytest**
    ```bash
    pip install pytest
    ```
    **Run the model to generate text**
    ```bash
    python src/generate.py
    ```
    This will:
    Load the corpus from data/example_corpus.txt
    Train the trigram model 
    Generate a sample text of up to 50 words

    **Run tests**
   ```bash
    pytest
    ```



## Design Choices

All design choices are explained in detail in the evaluation.md file.
It includes:
Text cleaning strategy
Tokenization
Padding tokens (<s>, </s>)
Data structures used for trigram counting
Probabilistic sampling method
How unknown words are handled
Generation logic
Testing approach
