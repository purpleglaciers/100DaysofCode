import pandas

# TODO 1. Create a dictionary in this format:

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Type a word you would like to convert to Nato Phonetic Alphabet: ").upper()
user_input_list = list(user_input)
user_output = [nato_alphabet_dict[letter] for letter in user_input_list]
print(user_output)


