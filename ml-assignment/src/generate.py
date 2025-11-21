from ngram_model import TrigramModel


def main():
    model = TrigramModel()

    
    with open("../data/example_corpus.txt", "r", encoding="utf-8") as f:
        text = f.read()

    model.fit(text)

    generated_text = model.generate()
    print("Generated Text:")
    print(generated_text)


if __name__ == "__main__":
    main()
