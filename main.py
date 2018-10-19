import math


def main(file_in, file_out, n):
    raw_text = bring_files(file_in, file_out)
    text_out = insertion(raw_text, int(n))
    text_to_file(file_out, text_out)


def bring_files(file_in, file_out):
    """bring files into program"""
    with open(file_in) as f1:
        with open(file_out) as f2:
            return f1.read(), f2.read()


def insertion(raw_text, n):
    """insert raw text of file_in to some proportion of raw text of file_out"""
    text_in = raw_text[0]
    text_out = raw_text[1]
    split_point = math.floor(n*len(text_out))
    return text_out[:split_point] + text_in + text_out[split_point:]


def text_to_file(file_out, text_out):
    """overwrite file_out"""
    with open(file_out, 'w') as f:
        f.write(text_out)
