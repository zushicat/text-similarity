# text-similarity

Use 2 methods to determine the similarity of 2 texts:
- get the (normalized) number of n-gram intersections
- get the (normalized) value of Longest Common Subsequences (LCS)


In the data directory you'll find following text examples:
- The source text: the first paragraph of the wikipedia article about Henry VIII
  - wikipedia_expl_source.txt
- Short target texts about the source paragraph with increasing modification
  - wikipedia_expl_target_strong.txt (almost copy&paste)
  - wikipedia_expl_target_moderate.txt (some modifications)
  - wikipedia_expl_target_weak.txt (very strong modifications)

This certainly can be further improved i.e. by more text cleaning before comparison such as eliminating stopwords.


## Usage
Call text_similarity.py to apply both methods on all examples.

If you like to run this inside an environment, change to "text-similarity" directory and call
```
$ pipenv install
```
Then change into environment with
```
$ pipenv shell
```
(Exit shell with "exit")


## Results
```
---------- target_strong ----------
n_gram intersections: 0.89
lcs: 0.99
Subsequence Lengths: max 20 | mean 8.62 | median 7.5

[
  "henry viii",
  "was king of england from 1509 until his death in 1547 henry is best known for his six marriages and",
  "his efforts to have his first marriage to catherine of aragon annulled",
  "henry viii",
  "is also known as the father of the royal navy as he invested heavily in the navy",
  "and established the navy board",
  "henry",
  "is known for his radical changes to the english constitution"
]

---------- target_moderate ----------
n_gram intersections: 0.64
lcs: 0.84
Subsequence Lengths: max 7 | mean 2.68 | median 2.0

[
  "henry viii",
  "was king of england",
  "until his death in 1547 henry is",
  "for his",
  "marriages",
  "efforts",
  "to",
  "catherine of aragon",
  "henry",
  "is",
  "the",
  "father of the royal navy",
  "he invested heavily in the navy",
  "increasing its size",
  "to more than 50 ships",
  "he",
  "also",
  "established the navy board",
  "henry",
  "is",
  "known for his",
  "changes to the english constitution"
]

---------- target_weak ----------
n_gram intersections: 0.37
lcs: 0.48
Subsequence Lengths: max 5 | mean 1.39 | median 1

[
  "henry viii",
  "england",
  "1509",
  "and",
  "when",
  "he",
  "from",
  "a",
  "death",
  "to",
  "his",
  "marriage to catherine of aragon",
  "and",
  "henry",
  "established the navy board",
  "and",
  "the",
  "royal",
  "as",
  "in",
  "the",
  "henry",
  "the english"
]
```
