class Solution(object):
    def searchInsert(self, nums, target):
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
      
      if target < nums[mid_val]:
        return mid_val
      else:
        return mid_val + 1

def example_1():
  nums = [1, 3, 5, 6]
  target = 5
  handler = Solution
  result = handler.searchInsert(handler, nums, target)
  assert result == 2
  print("Example 1 result: " + str(result) + "!")

def example_2():
  nums = [1, 3, 5, 6]
  target = 2
  handler = Solution
  result = handler.searchInsert(handler, nums, target)
  assert result == 1
  print("Example 2 result: " + str(result) + "!")

def example_3():
  nums = [1, 3, 5, 6]
  target = 7
  handler = Solution
  result = handler.searchInsert(handler, nums, target)
  assert result == 4
  print("Example 3 result: " + str(result) + "!")

example_1()
example_2()
example_3()