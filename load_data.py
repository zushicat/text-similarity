import string
import typing

def get_cleaned_text(file_name: str) -> str: 
    def clean_text(original_text):
        cleaned_token = original_text.lower().replace("\n", " ").split()  # lower text / no paragraphs
        for i, token in enumerate(cleaned_token):  # get rid of any puncctuation
            for p in string.punctuation:
                token = token.replace(p, " ")
            cleaned_token[i] = "".join(token)
        cleaned_token = [x.strip() for x in cleaned_token if len(x) > 0]
        return " ".join(cleaned_token)
    
    with open(f"data/{file_name}") as f:
        original_text = f.read()
    return clean_text(original_text)