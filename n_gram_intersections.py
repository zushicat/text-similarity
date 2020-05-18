from typing import Dict

from load_data import get_cleaned_text

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

def get_intersections(source_text: str, target_text: str, n: int) -> float:
    vectorizer = CountVectorizer(analyzer='word', ngram_range=(1, n))
    vocab = vectorizer.fit([source_text, target_text]).vocabulary_
    counts = vectorizer.fit_transform([source_text, target_text])

    intersection_n_grams = np.amin(counts.toarray(), axis = 0)
    intersection_sum = np.sum(intersection_n_grams) # summing the intersection count
    count_ngram_target_text = np.sum(counts.toarray()[1]) # num n-grams in target

    return round(intersection_sum / count_ngram_target_text, 2)  # normalized containment value


if __name__ == '__main__':
    # ***
    # <source> is the base text (i.e. wikipedia article) which is then compared to different <targets>
    texts: Dict[str, str] = {}
    for key, file_name in [
            ("source", "wikipedia_expl_source.txt"),
            ("target_strong", "wikipedia_expl_target_strong.txt"),
            ("target_moderate", "wikipedia_expl_target_moderate.txt"),
            ("target_weak", "wikipedia_expl_target_weak.txt")
        ]:
        texts[key] = get_cleaned_text(file_name)

    # ***
    #
    n = 3
    for target in ["target_strong", "target_moderate", "target_weak"]:
        intersection_value = get_intersections(texts["source"], texts[target], n)
        print(f"{target}: {intersection_value}")
