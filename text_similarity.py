import json
from lcs import lcs_with_text
from load_data import get_cleaned_text
from n_gram_intersections import get_intersections
from typing import Dict


if __name__ == '__main__':
    '''
    Get example texts: 
    - source text is an wikipedia excerpt about Henry VIII
    - target texts are 3 short texts about this short paragraph with different ranges of similarity to the source text

    Compare source and target:
    - Get similarity by comparing n-gram word intersections
    - Get Longest Common Subsequence incl. found subtext strings (lcs)
    '''
    texts: Dict[str, str] = {}
    for key, file_name in [
            ("source", "wikipedia_expl_source.txt"),
            ("target_strong", "wikipedia_expl_target_strong.txt"),
            ("target_moderate", "wikipedia_expl_target_moderate.txt"),
            ("target_weak", "wikipedia_expl_target_weak.txt")
        ]:
        texts[key] = get_cleaned_text(file_name)
    
    for target in ["target_strong", "target_moderate", "target_weak"]:
        # ***
        # get similarity by n-gram word intersections
        n = 3  # max bi-gram len
        intersection_value: float = get_intersections(texts["source"], texts[target], n)
        
        # ***
        # get similarity (and subsequence strings) by lcs
        lcs_value, lcs_str_list, str_max_len, str_mean_len, str_median_len = lcs_with_text(texts["source"], texts[target])

        print(f"---------- {target} ----------")
        print(f"n_gram intersections: {intersection_value}")
        print(f"lcs: {lcs_value}")
        print(f"Subsequence Lengths: max {str_max_len} | mean {str_mean_len} | median {str_median_len}")
        print()
        print(json.dumps(lcs_str_list, indent=2))
        print()
