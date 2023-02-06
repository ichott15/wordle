import time

def load_words():
    with open('wordle-dictionary.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def input_and_hide(prompt):
    input_text = input("         " + prompt + "\r")
    time.sleep(1)
    print("   " * 20)

    return input_text


