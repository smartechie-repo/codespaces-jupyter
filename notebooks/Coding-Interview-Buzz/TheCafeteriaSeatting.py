# A cafeteria table consists of a row of N seats, numbered from 1 to N from left to right. Social distancing guidelines require that every diner be seated such that K seats to their left and K seats to their right (or all the remaining seats to that side if there are fewer than K) remain empty.
# There are currently M diners seated at the table, the ith of whom is in seat Si. No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.
# Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.
# Please take care to write a solution which runs within the time limit.

# Constraints
# 1≤N≤10^15
# 1≤K≤N1
# 1≤M≤500,0001
# M≤N
# 1≤Si≤N

# Sample test case #1
# N = 10
# K = 1
# M = 2
# S = [2, 6]

# Expected Return Value = 3

# Sample Explanation
# In the first case, the cafeteria table has N=10N = 10N=10 seats, with two diners currently at seats 222 and 666 respectively. The table initially looks as follows, with brackets covering the K=1K = 1K=1 seat to the left and right of each existing diner that may not be taken.

# 1 2 3 4 5 6 7 8 9 10
# [ ] [ ]

# Three additional diners may sit at seats 4, 8, and 10 without violating the social distancing guidelines.


from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  S.sort()
  num_new_diners = (S[0] - 1) // (K + 1)
  for i in range(1, len(S)):
    num_new_diners += (S[i] - S[i-1] - K-1) // (K + 1)
  num_new_diners += (N - S[-1]) // (K + 1)
  return num_new_diners


