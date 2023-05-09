## Load up dictionary.txt
with open('dictionary.txt', 'r') as file:
  dictionary_words = []
  for line in file:
    line = line.strip()
    dictionary_words.append(line)

