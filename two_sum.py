# naive solution
class Solution_1:
  def twoSum(self, numbers: list[int], target: int) -> list[int]:
    result = []
    n = len(numbers)
    for i in range(n):
      for j in range(i+1, n):
        if numbers[i] + numbers[j] == target:
          result.append(i+1)
          result.append(j+1)
          return result
        elif numbers[i] + numbers[j] > target:
          break

    return result

# efficient solution for ordered list
class Solution_2:
  def twoSum(self, numbers: list[int], target: int) -> list[int]:
    result = []
    n = len(numbers)
    left = 0
    right = n-1
    while left < right:
      if numbers[left] + numbers[right] == target:
        result.append(left+1)
        result.append(right+1)
        return result
      elif numbers[left] + numbers[right] < target:
        left += 1
      else:
        right -= 1

    return result

def check_result(result, expected_result):
  n = len(result)
  for i in range(n):
    assert result[i] == expected_result[i]

def example_1():
  numbers = [2, 7, 11, 15]
  target = 9
  expected_result = [1, 2]
  solution_handler = Solution_2
  result = solution_handler.twoSum(solution_handler, numbers, target)
  check_result(result, expected_result)
  print("The result for example 1 is: " + str(result))

def example_2():
  numbers = [2, 3, 4]
  target = 6
  expected_result = [1, 3]
  solution_handler = Solution_2
  result = solution_handler.twoSum(solution_handler, numbers, target)
  check_result(result, expected_result)
  print("The result for example 2 is: " + str(result))

def example_3():
  numbers = [-1, 0]
  target = -1
  expected_result = [1, 2]
  solution_handler = Solution_2
  result = solution_handler.twoSum(solution_handler, numbers, target)
  check_result(result, expected_result)
  print("The result for example 3 is: " + str(result))

example_1()
example_2()
example_3()