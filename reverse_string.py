class Solution:
  def reverseString(self, s: list[str]) -> None:
    n = len(s)-1
    r = len(s)//2
    for i in range(r):
      tmp = s[i]
      s[i] = s[n-i]
      s[n-i] = tmp

def check_result(result, expected_result):
  n = len(result)
  for i in range(n):
    assert result[i] == expected_result[i]

def example_1():
  s = ["h", "e", "l", "l", "o"]
  expected_result = ["o", "l", "l", "e", "h"]
  solution_handler = Solution
  solution_handler.reverseString(solution_handler, s)
  check_result(s, expected_result)
  print("The result for example 1 is: " + str(s))

def example_2():
  s = ["H", "a", "n", "n", "a", "h"]
  expected_result = ["h", "a", "n", "n", "a", "H"]
  solution_handler = Solution
  solution_handler.reverseString(solution_handler, s)
  check_result(s, expected_result)
  print("The result for example 2 is: " + str(s))

example_1()
example_2()