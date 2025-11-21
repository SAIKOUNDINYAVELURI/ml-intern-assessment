# Evaluation

**Trigram Language Model – Design Choices**
**N-gram Storage**
For storing trigram counts, I used a nested dictionary structure: the outer dictionary maps the first word to a dictionary of second words, which in turn maps to a dictionary of third words with their occurrence counts. This structure allows efficient lookup and probability computation for any trigram, and it scales well for medium-sized corpora.

**Probabilistic Text Generation**
The generate function creates text sequences by probabilistically sampling the next word based on trigram probabilities. Starting with the <s> tokens, the model looks up the trigram counts, computes the conditional probabilities, and randomly selects the next word. This process continues until the end-of-sentence token </s> is generated or a specified maximum length is reached.

**Additional Decisions**
**Smoothing**: To handle zero probabilities for unseen trigrams, I implemented add-one (Laplace) smoothing, ensuring all possible trigrams have a non-zero probability.

**Efficiency**: Count storage and probability calculation are optimized to avoid repeated computations during generation.

**Extensibility**: The design supports easy expansion to higher-order n-grams or integration with larger corpora.

Overall, the design focuses on simplicity, efficiency, and robustness while producing realistic text sequences.
