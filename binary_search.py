class Solution:
  def search(self, nums: list[int], target: int) -> int:
    for i in range(len(nums)):
      if nums[i] == target:
        return i
    return -1

def example_1():
  nums = [-1, 0, 3, 5, 9, 12]
  target = 9
  handler = Solution
  result = handler.search(handler, nums, target)
  assert result == 4
  print("Example 1 result: " + str(result) + "!")

def example_2():
  nums = [-1, 0, 3, 5, 9, 12]
  target = 2
  handler = Solution
  result = handler.search(handler, nums, target)
  assert result == -1
  print("Example 2 result: " + str(result) + "!")

example_1()
example_2()