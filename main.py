# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)    -> Prints out the dictionary therefore usefull for debugging


def generate_phonetic():
    while True:
        word = input("Enter a word: ").strip().upper()

        if not word:
            print("Please enter a word.")
            continue

        try:
            output_list = [phonetic_dict[letter] for letter in word]

        except KeyError:
            print("Sorry, only letters in the alphabet please.")

        else:
            print(output_list)
            break

generate_phonetic()
