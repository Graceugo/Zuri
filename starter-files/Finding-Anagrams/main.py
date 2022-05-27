# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
  str1 = "smile"
  str2 = "miles"
  str1_word = sorted(str1)
  str2_anagram = sorted(str2)

  if str_word == str_anagram:
     return True
  else:
     return False
print(find_anagram("smile", "miles"))

