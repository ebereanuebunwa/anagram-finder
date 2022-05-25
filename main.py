# Check if two words are anagrams 

first_word = input('First word: ')
second_word = input('Second word: ')


def find_anagram(word, anagram):
    # for two words to be anagrams, they must meet certain criteria:
    # 1. They must have the same set of letters.
    # 2. Each letter is positioned differently in each word.
    # 3. Both words are equal in length.

    # append all the letters in word and anagram to two separate lists.
    word_list = [letter.lower() for letter in word if letter != ' ']
    anagram_list = [letter.lower() for letter in anagram if letter != ' ']

    # sort both lists to have uniform arrangements using the sorted() function 
    sorted_word_list = sorted(word_list)
    sorted_anagram_list = sorted(anagram_list)

    # if both lists are not equal after sorting, then the two words 
    # are not anagrams.
    # Use an if-statement
    if sorted_word_list != sorted_anagram_list:
        return False

    return True


if find_anagram(first_word, second_word):
    print('Both words are anagrams.')
else:
    print('They are not anagrams.')
