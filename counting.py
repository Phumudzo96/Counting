string = input("Enter input/word: ")              # ask a user to enter an input

counter = {}                                      # create a variable with empty parentheses

for words in string:                              # for the words that are entered in the input
    if words in counter:                          # the input must be entered in the parentheses
        counter[words] += 1                       # eveytime a word that is counter is seen, 1 must be added
    else:
        counter[words] = 1                        # all words in counter will equal 1
print(counter)