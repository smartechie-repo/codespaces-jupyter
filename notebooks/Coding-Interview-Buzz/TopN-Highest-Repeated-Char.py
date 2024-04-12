
# In this coding task, candidates are tasked with implementing a method, `mostRepeatedCharacters`.
# This method identifies the most frequently occurring characters in a given string and their respective frequencies.

from collections import Counter

def most_repeated_characters_using_counter(text, topN=1):
  """
  Finds the most frequently occurring characters in a string and their frequencies.

  Args:
      text: The input string.

  Returns:
      A dictionary mapping characters to their frequencies.
  """

  char_counts = Counter(text)
  # Get the most frequent character(s) and their count
  most_frequent = char_counts.most_common(topN)

  # print("most_frequent list: ", most_frequent)
  return most_frequent

from collections import OrderedDict
def most_repeated_characters_using_hashmap(text, topN=1):
  """
  Finds the most frequently occurring characters in a string and their frequencies.

  Args:
      text: The input string.

  Returns:
      A dictionary mapping characters to their frequencies.
  """

  char_counts = {}
  for idx in range(len(text)):
    ch  = text[idx]
    if ch in char_counts:
      char_counts[text[idx]] += 1 
    else:
      char_counts[text[idx]] = 1 
  # Get the most frequent character(s) and their count
  most_frequent = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

  # print("most_frequent list: ", most_frequent)
  return most_frequent[:topN]

text = "Get the most frequent character(s) and their count"
topN=3
print("*"*50)
result = most_repeated_characters_using_hashmap(text, topN)
print(f"Top {topN} frequently occured characters & count (USING COUNTER): ", result)
print("*"*50)
result = most_repeated_characters_using_hashmap(text, topN)
print(f"Top {topN} frequently occured characters & count (USING HASHMAP): ", result)