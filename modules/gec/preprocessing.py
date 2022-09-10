def preprocessing_pipeline(doc: str) -> str:
    doc = [sentence for sentence in doc.split("\n")]
    # convert multi whitespaces to single one
    doc = [" ".join(sentence.split()) for sentence in doc]
    doc = [sentence for sentence in doc if len(sentence) > 0]
    doc = "\n".join(doc)
    return doc


if __name__ == "__main__":
    text = "a b  c\n\nd e. f\ng.h"
    print(text)
    print("=" * 100)
    print(preprocessing_pipeline(text))
