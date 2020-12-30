VOWELS = ['a','e','i','o','u']


def input_string_to_translate_to_pig_latin(prompt):
    return input(prompt).strip().lower()

def split_str(input_str):
    return input_str.split()

def translate_to_pig_latin(words):
    pig_latin_str = ''
    for word in words:
        if word[0] in VOWELS:
           pig_latin_str = word + 'way'
           continue
    print('===================', pig_latin_str)

def main():
    user_input = input_string_to_translate_to_pig_latin('What would you like to translate to pig latin? ')
    list_of_words = split_str(user_input)
    translate_to_pig_latin(list_of_words)

main()
