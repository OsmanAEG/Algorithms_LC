class Solution:
  def __init__(self, bad_val):
    self.bad_val = bad_val
  
  def isBadVersion(self, version):
    if version < self.bad_val:
      return False
    return True

  # sequential binary search
  def firstBadVersion(self, n):
    min_val = 0
    max_val = n

    while min_val <= max_val:
      mid_val = min_val + (max_val-min_val)//2
      if self.isBadVersion(mid_val):
        max_val = mid_val - 1
      else:
        min_val = mid_val + 1
    return min_val

def example_1():
  n = 5
  bad = 4
  solution_handler = Solution(bad)
  result = solution_handler.firstBadVersion(n)
  assert result == 4
  print("The result for example 1 is: " + str(result) + "!")

def example_2():
  n = 1
  bad = 1
  solution_handler = Solution(bad)
  result = solution_handler.firstBadVersion(n)
  assert result == 1
  print("The result for example 2 is: " + str(result) + "!")

example_1()
example_2()
      
        

        