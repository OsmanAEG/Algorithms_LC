class Solution:
  def bubble_sort(unsorted_list):
    n = len(unsorted_list) - 1
    for i in range(n):
      for j in range(n-i):
        if unsorted_list[j] > unsorted_list[j+1]:
          tmp = unsorted_list[j]
          unsorted_list[j] = unsorted_list[j+1]
          unsorted_list[j+1] = tmp
          
  def sortedSquares(self, nums):
    n = len(nums)
    squared = [int]*n
    
    # squaring listed values
    for i in range(n):
      squared[i] = nums[i]**2 

    self.bubble_sort(squared)
    # alternatively: squared.sort()

    return squared

def check_result(result, expected_result):
  n = len(result) - 1
  for i in range(n):
    assert result[i] == expected_result[i]

def example_1():
  nums = [-4, -1, 0, 3, 10]
  solution_handler = Solution
  expected_result = [0, 1, 9, 16, 100]
  result = solution_handler.sortedSquares(solution_handler, nums)
  check_result(result, expected_result)
  print("The result for example 1 is: " + str(result))

def example_2():
  nums = [-7, -3, 2, 3, 11]
  solution_handler = Solution
  expected_result = [4, 9, 9, 49, 121]
  result = solution_handler.sortedSquares(solution_handler, nums)
  check_result(result, expected_result)
  print("The result for example 2 is: " + str(result))

example_1()
example_2()