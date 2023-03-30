# binary search
class Solution:
  def search(self, nums: list[int], target: int) -> int:
    min_val = 0
    max_val = len(nums) - 1

    while min_val <= max_val:
      mid_val = min_val + (max_val-min_val)//2
      mid_nums = nums[mid_val]
      if(nums[mid_val] == target):
        return mid_val
      elif mid_nums < target:
        min_val = mid_val + 1
      else:
        max_val = mid_val - 1
    
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