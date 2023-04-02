class Solution:
  def moveZeroes(self, nums: list[int]) -> None:
    i = 0
    c = 0
    n = len(nums)
    while c < n:
      if nums[i] == 0:
        nums.pop(i)
        nums.append(0)
        i -= 1
      i += 1
      c += 1
    return nums

def check_result(result, expected_result):
  n = len(result)
  for i in range(n):
    assert result[i] == expected_result[i]

def example_1():
  nums = [0, 1, 0, 3, 12]
  expected_result = [1, 3, 12, 0, 0]
  solution_handler = Solution
  result = solution_handler.moveZeroes(solution_handler, nums)
  check_result(result, expected_result)
  print("The result for example 1 is: " + str(result))

def example_2():
  nums = [0]
  expected_result = [0]
  solution_handler = Solution
  result = solution_handler.moveZeroes(solution_handler, nums)
  check_result(result, expected_result)
  print("The result for example 2 is: " + str(result))

def example_test():
  nums = [0, 0, 1]
  expected_result = [1, 0, 0]
  solution_handler = Solution
  result = solution_handler.moveZeroes(solution_handler, nums)
  check_result(result, expected_result)
  print("The result for example test is: " + str(result))

example_1()
example_2()
example_test()