
"""Count words in file."""

# open the file
# create an empty dictionary
# split the words by empty space
# iterate over each word and save into the dict

data = open("test.txt")

word_count = {}

for line in data:
    line = line.rstrip()

    words = line.split()

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"Word: {word}, count: {count}")







