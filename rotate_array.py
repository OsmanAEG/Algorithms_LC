# naive implementation
class Solution_1:
  def shift_one_time(unshifted_list):
    tmpi = unshifted_list[0]
    tmpn = unshifted_list[-1]

    for i in range(1, len(unshifted_list)):
      tmp = unshifted_list[i]
      unshifted_list[i] = tmpi
      tmpi = tmp

    unshifted_list[0] = tmpn

  def rotate(self, nums, k):
    for i in range(k):
      self.shift_one_time(nums)

    return nums

class Solution_2:
  def rotate(self, nums, k):
    shifted_nums = []
    n = len(nums)

    if n > 1 and n != k:
      start = 0
      end = 0

      if n > k:
        start = n-k
        end = n
      else:
        start = n - (k-n)
        end = n

      # add the end of the list
      for i in range(start, end):
        shifted_nums.append(nums[i])

      # add the begining of the list
      for i in range(start):
        shifted_nums.append(nums[i])

      for i in range(n):
        nums[i] = shifted_nums[i]

    return nums

def check_result(result, expected_result):
  n = len(result)
  for i in range(n):
    assert result[i] == expected_result[i]

def example_1():
  nums = [1, 2, 3, 4, 5, 6, 7]
  k = 3
  expected_result = [5, 6, 7, 1, 2, 3, 4]
  solution_handler = Solution_2
  result = solution_handler.rotate(solution_handler, nums, k)
  check_result(result, expected_result)
  print("The result for example 1 is: " + str(result))

def example_2():
  nums = [-1, -100, 3, 99]
  k = 2
  expected_result = [3, 99, -1, -100]
  solution_handler = Solution_2
  result = solution_handler.rotate(solution_handler, nums, k)
  check_result(result, expected_result)
  print("The result for example 2 is: " + str(result))

def example_test():
  nums = [1, 2, 3]
  k = 4
  solution_handler = Solution_2
  result = solution_handler.rotate(solution_handler, nums, k)
  print("The result for example test is: " + str(result))

example_1()
example_2()
example_test()


