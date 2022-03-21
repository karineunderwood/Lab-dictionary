#make a function
#open a file, count how many times each space-separated word occurs in the file
#return eaech word and the number of times it occurs
#close the file

def word_count(file):
    file_to_open = open(file)

    # for line in file_to_open:
    #     line.rstrip()
    #     line.split()
    #     for char in line:
    #         empty_str = ""
    #         print(char)
    #         if char.isalpha():
    #             empty_str += char
    #         elif char == " ":
    #             empty_str += " "
    #         else:
    #             char = ""
    #     print(empty_str)
    
    for line in file_to_open:
        line = line.rstrip()
        words = line.split()
        how_many_words_dict = {}
        for word in words:
            # if not word[-1].isalpha():
            #     word = word[:-1]
            how_many_words_dict[word] = how_many_words_dict.get(word, 0) + 1
            # else:
            #     how_many_words_dict[word] = how_many_words_dict.get(word, 0) + 1



        print(f'{how_many_words_dict}')

            
            # if char == char.isalpha():
            #     char = ""
            # print(char)
                
      


word_count("test.txt")
"""Count words in file."""


# put your code here.
