import json
from statistics import mean, median
from typing import Dict, List, Tuple

from load_data import get_cleaned_text
import numpy as np

def lcs_simple(source_text: str, target_text: str) -> int:
    '''
    Calculate lcs matrix and return normalized lcs value
    '''
    source_token: List[str] = source_text.split()
    target_token: List[str] = target_text.split()

    num_cols = len(source_token) 
    num_rows = len(target_token) 

    matrix = [[0]*(num_rows + 1) for i in range(num_cols + 1)]  # make matrix filled with 0 (one extra top, left)
    
    for col in range(num_cols + 1): 
        if col == 0:  # skip first empty col
            continue
        for row in range(num_rows + 1): 
            if row == 0:  # skip first empty row
                continue
            # ***
            # the actual comparison part
            if source_token[col-1] == target_token[row-1]: 
                matrix[col][row] = matrix[col-1][row-1]+1  # top left diag. value + 1
            else: 
                matrix[col][row] = max(matrix[col-1][row], matrix[col][row-1])  # max value: top, left
    
    return round(matrix[-1][-1]/len(target_token), 2)  # very last value in matrix is abs. lcs value


def lcs_with_text(source_text: str, target_text: str) -> Tuple[float, List[str], int, float, float]:
    '''
    Calculate lcs matrix (same as above) and additionally store equal substrings in list
    '''
    source_token: List[str] = source_text.split()
    target_token: List[str] = target_text.split()

    num_cols = len(source_token) 
    num_rows = len(target_token) 

    matrix = [[0]*(num_rows + 1) for i in range(num_cols + 1)]  # make matrix filled with 0 (one extra top, left)
    
    for col in range(num_cols + 1): 
        if col == 0:  # skip first empty col
            continue
        for row in range(num_rows + 1): 
            if row == 0:  # skip first empty row
                continue
            # ***
            # the actual comparison part
            if source_token[col-1] == target_token[row-1]: 
                matrix[col][row] = matrix[col-1][row-1]+1  # top left diag. value + 1
                last_max_indices = [col, row]
            else: 
                matrix[col][row] = max(matrix[col-1][row], matrix[col][row-1])  # max value: top, left
    
    lcs_value: float = round(matrix[-1][-1]/len(target_token), 2)  # normalize abs. lccs value (last in matrix)
    
    col: int = num_cols
    row: int = num_rows
    
    lcs_token: List[List[str]] = [[]]
    
    while col > 0 and row > 0: 
        if source_token[col-1] == target_token[row-1]:  # token at position are equal: store and move cursor (top, left)
            lcs_token[0].insert(0, source_token[col-1])  # prepend token to current list
            col -= 1
            row -= 1
        else:  
            # new sublist of consecutive token (can also be len == 1)
            if len(lcs_token[0]) > 0:
                lcs_token.insert(0, [])  # prepend new list

            # find max. value (top or teft) and move to this position
            if matrix[col-1][row] > matrix[col][row-1]:  # value left > value top: move left 
                col -= 1
            else: 
                row -= 1  # move top
    
    # some additional mini statistics on stored substrings
    max_len: int = len(max(lcs_token, key=len))
    mean_len: float = round(mean([len(x) for x in lcs_token]), 2)
    median_len: float = round(median([len(x) for x in lcs_token]), 2)
    
    # create list of str (from sublists of token)
    lcs_str_list: List[str] = []
    for sublist in lcs_token:
        lcs_str_list.append(" ".join(sublist))
    
    return lcs_value, lcs_str_list, max_len, mean_len, median_len


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
    
    # mini test with hardcoded texts
    # lcs_value, lcs_str = lcs_with_text(
    #     "Henry VIII was King of England from 1509 until his death in 1547".lower(), 
    #     "Henry VIII reigned England between 1509 and 1547 when he died from a natural death".lower()
    # )

    # check short, loaded test texts with loaded source text
    for target in ["target_strong", "target_moderate", "target_weak"]:
        lcs_value, lcs_str_list, max_len, mean_len, median_len = lcs_with_text(texts["source"], texts[target])
        
        print(f"--------- {target} ---------")
        print(f"lcs: {lcs_value} | max: {max_len} | mean: {mean_len} | median: {median_len}")
        print(json.dumps(lcs_str_list, indent=2))
        print()
