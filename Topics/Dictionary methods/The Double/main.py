import string

string_list = list(string.ascii_lowercase)
double_alphabet = {char: char * 2 for char in string_list}
