import random
import re
from collections import defaultdict

class TrigramModel:
    def __init__(self):
        
        self.trigram_counts = defaultdict(lambda: defaultdict(int))
        self.vocab = set()
        self.trained = False

    def _clean_text(self, text):
      
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s\.]", "", text)
        return text

    def _tokenize(self, text):
      
        return text.split()

    def fit(self, text):

        if not text.strip():
            self.trained = False
            return

        text = self._clean_text(text)
        tokens = self._tokenize(text)

        if len(tokens) < 2:
            self.trained = False
            return

        self.vocab = set(tokens)

        # Add padding tokens
        padded = ["<s>", "<s>"] + tokens + ["</s>"]

        # Count trigrams
        for i in range(len(padded) - 2):
            w1, w2, w3 = padded[i], padded[i+1], padded[i+2]
            self.trigram_counts[(w1, w2)][w3] += 1

        self.trained = True

    def _sample_next(self, context):
       
        options = self.trigram_counts.get(context)

        if not options:
            return random.choice(list(self.vocab)) if self.vocab else ""

        words = list(options.keys())
        counts = list(options.values())
        total = sum(counts)
        probs = [c / total for c in counts]

        return random.choices(words, weights=probs, k=1)[0]

    def generate(self, max_length=50):
        
        if not self.trained:
            return ""

        w1, w2 = "<s>", "<s>"
        output = []

        for _ in range(max_length):
            next_word = self._sample_next((w1, w2))

            if next_word == "</s>":
                break

            output.append(next_word)
            w1, w2 = w2, next_word

        return " ".join(output)
