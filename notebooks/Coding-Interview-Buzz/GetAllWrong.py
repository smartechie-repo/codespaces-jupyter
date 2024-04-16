# There's a multiple-choice test with N questions, numbered from 1 to N. Each question has answer options, labelled A and B. You know that the correct answer for the ith question is the ith character in the string 
#  C, which is either "A" or "B".
# Your task is to implement the function getWrongAnswers(N, C) which returns a string with N characters, the ith of which is the answer you should give for question i in order to get it wrong (either "A" or "B").

# Constraints

# ∈{‘‘A",‘‘B"}
# Sample test case #1
# N = 3
# C = ABA
# Expected Return Value = BAB
# Sample test case #2
# N = 5
# C = BBBBB
# Expected Return Value = AAAAA
# Sample Explanation
# In the first case the correct answers to the questions are A, B, and A, in that order. Therefore, in order to get them all wrong, the answers you should give are B, A, and B, in that order.
# In the second case the correct answers are all B, so you should answer each question with A.




def getWrongAnswers(N: int, C: str) -> str:
  result = ""
  for i in range(len(C)):
    if i < N:
      if C[i] == 'A':
        C = C[:i] + 'B' + C[i+1:]
      elif C[i] == 'B':
         C = C[:i] + 'A' + C[i+1:]
    print(result)
  return C
