# """
# NON-STARTER CODE
#
# JUST RUN
# `python3 word_jumble_1.py`
# IN THE TERMINAL
# """

# from words_list import dictionary_words
# from histogram_generator import histogram_generator

# letter_bank = []

# def dejumbler(str_to_unjumble, circled_positions=[]):
#   str_len = len(str_to_unjumble)
#   filtered_by_len = list(filter(lambda word: len(word) == str_len, dictionary_words))

#   main_str_hist = histogram_generator(str_to_unjumble)

#   found_word = ''
#   for word in filtered_by_len:
#     curr_histogram = histogram_generator(word)
#     if main_str_hist == curr_histogram:
#       found_word = word
#       break
#   if found_word == '':
#     # print('Not found in english dictionary!')
#     return None

#   # print(f"{found_word}: {curr_histogram}")
#   if len(circled_positions):
#     chosen_letters = []
#     for index in circled_positions:
#       chosen_letters.append(found_word[index])
#     return chosen_letters
#   else:
#     return found_word



# # input: (word, circled_positions)
# to_dejumble = [
#   dejumbler('tefon', [2, 4]),
#   dejumbler('sokik', [0, 1, 3]),
#   dejumbler('niumem', [4]),
#   dejumbler('siconu', [3, 4]),
# ]

# for letters in to_dejumble:
#   letter_bank.extend(letters)

# # print(letter_bank)
# # # ['t', 'n', 'k', 'i', 's', 'n', 's', 'i']

# """
# 2nd part Algorithm:
#   brute force loop a bunch of 2 letter words, and other find english words with the remainders. store those all
#   tn, nope
#   tk, nope
#   it, yes, so find all combos of n, k, s, n, s, i
#   ... (cache all of these as I go along?)
#   nk, no
#   in, yes, so find all combos of t, k, s, n, s, i
# """

# def final_jumble(letter_bank):
#   seen = {}
#   remaining_letters = ''
#   for i, letter_i in enumerate(letter_bank):
#     for j, letter_j in enumerate(letter_bank):
#       if i == j:
#         continue
#       elif i < j:
#         remaining_letters = letter_bank[:i] + letter_bank[i+1:j] + letter_bank[j+1:]
#       elif i > j:
#         remaining_letters = letter_bank[:j] + letter_bank[j+1:i] + letter_bank[i+1:]
#       if letter_i == letter_j:
#         # skip if same letter
#         continue
#       two_letter_word = letter_i + letter_j
#       if two_letter_word in seen:
#         # skip if exists in cache
#         continue
#       else:
#         # check if two_letter_word is in english dictionary
#         found_two_letter_word = dejumbler(two_letter_word)
#         if found_two_letter_word is not None:
#           found_second_word = dejumbler(remaining_letters)
#           if found_second_word is not None:
#             seen[two_letter_word] = found_second_word
#         else:
#           seen[two_letter_word] = 'Not a two letter word'
#   print(seen)
#   return seen

# print("possible choices:")
# final_jumble(letter_bank)

# """
# PRINTS OUT:
# {
#   'tn': 'siskin',
#   'ts': 'kinins',
#   'nt': 'siskin',
#   'nk': 'insist',
#   'ni': 'stinks',
#   'kn': 'insist',
#   'in': 'stinks', <-- ANSWER
#   'st': 'kinins'
# }
# """
