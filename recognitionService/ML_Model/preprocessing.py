import pandas as pd
import re
import string

# https://github.com/motazsaad/process-arabic-text/blob/f950f9b3aeba13ac3c16cd10502a8eafbdfa1262/clean_arabic_text.py
# I found this useful and quick to use, I hope it doesn't violate the task guideline.
# I'm using it and I know how it works and I'm referring to the links for fidelity.

# I modified methods that remove unwanted characters by replacing with empty string
# to replace with a space, and then a final step to remove redudant white spaces.

arabic_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
english_punctuations = string.punctuation
punctuations_list = arabic_punctuations + english_punctuations
punctuations_map = {p:' ' for p in punctuations_list}

def remove_diacritics(text):
    arabic_diacritics = re.compile("""
                 ّ    | # Tashdid
                 َ    | # Fatha
                 ً    | # Tanwin Fath
                 ُ    | # Damma
                 ٌ    | # Tanwin Damm
                 ِ    | # Kasra
                 ٍ    | # Tanwin Kasr
                 ْ    | # Sukun
                 ـ     # Tatwil/Kashida
             """, re.VERBOSE)
    return re.sub(arabic_diacritics, '', text)


def normalize_arabic(text):
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    text = re.sub("ة", "ه", text)
    text = re.sub("گ", "ك", text)
    return text


def remove_punctuations(text):
#     translator = str.maketrans('', '', punctuations_list)
    translator = str.maketrans(punctuations_map)
    return text.translate(translator)


def remove_repeating_char(text):
    # I found skipping هههه is better
    # this actually have some meaning/sentiment
    text = re.sub(r'([^ه])\1+', r'\1', text)
    # but then remove redundant هه more than, say 5
    # this is a common limit.
    # the pattern might be distorted, but it counts
    # correctly {4,}
    return re.sub(r'(ه)\1{4,}', r'\1\1\1\1', text)


def remove_mentions_links(text):
    # https://stackoverflow.com/a/56659272/12896502
    mention_links_pattern = re.compile(r'(@|https?)\S+|#')
    return mention_links_pattern.sub(r' ', text)


def remove_emojis(text):
    # https://stackoverflow.com/a/33417311/12896502
#     emojis_pattern = re.compile("["
#             u"\U0001F600-\U0001F64F"  # emoticons
#             u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#             u"\U0001F680-\U0001F6FF"  # transport & map symbols
#             u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#                                "]+", flags=re.UNICODE)
    # more emoji, previous wasn't enough, hopefully not an overkill
    # https://stackoverflow.com/a/58356570/12896502
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return emoj.sub(' ', text)


def remove_newlines(text):
    return re.sub(r'\n', ' ', text)


def remove_whitespaces(text):
    return re.sub(r'\s+', ' ', text)


def clean(text):
    pipeline = [
        remove_emojis,
        remove_mentions_links,
        remove_diacritics,
        normalize_arabic,
        remove_punctuations,
        remove_newlines,
        remove_repeating_char,
        remove_whitespaces,
    ]
    
    clean_text = text
    for step in pipeline:
        clean_text = step(clean_text)
    return clean_text.strip()
