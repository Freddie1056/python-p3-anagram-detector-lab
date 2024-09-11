# your code goes here!
class Anagram:
    def __init__(self, word):
        # Initialize with the word, convert to lowercase to handle case-insensitivity
        self.word = word.lower()

    def match(self, word_list):
        # Find all anagrams
        result = []
        sorted_word = sorted(self.word)  # Sort the letters of the original word
        for possible_anagram in word_list:
            # Compare sorted version of each possible anagram
            if sorted(possible_anagram.lower()) == sorted_word:
                result.append(possible_anagram)
        return result
