# Check if sum of any 2 integers exist in Array, equals to a given a given number.
# Given an array A[] of n numbers and another number x, 
# the task is to check whether or not there exist two elements in A[] whose sum is exactly x. 

# Examples: 

# Input: arr[] = {0, -1, 5, 3, 2, -3, 6, 1}, x= -2
# Output: Tow-Sum Exists !!!
# Explanation: If we calculate the sum of the output,1 + (-3) = -2

# Input: arr[] = {9, 1, -2, 1, 7, 4, 0, 5}, x = 0
# Output: Tow-Sum Doesn't Exist !!!

def find_pairs(arr, target_sum):
  """
  Finds pairs in the array that add up to the target sum using a hash table.

  Args:
      arr: A list of integers.
      target_sum: The target sum to find pairs for.

  Returns:
      True if a pair is found, False otherwise.
  """

  seen = set()
  for num in arr:
    complement = target_sum - num
    if complement in seen:
      return True
    seen.add(num)
  return False

# Driver code
A = [0, 1, 4, 5, 88, 6, 10, 8, 15, 100]
target_sum = 16
# output should be "Exists !!!" i.e 6 + 10 = 16
if find_pairs(A, target_sum):
  print("Tow-Sum Exists !!!")
else:
  print("Tow-Sum Doesn't Exist !!!")