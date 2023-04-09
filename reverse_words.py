# naive solution
class Solution_1:
  def reverseString(s):
    n = len(s)-1
    r = len(s)//2
    for i in range(r):
      tmp = s[i]
      s[i] = s[n-i]
      s[n-i] = tmp

  def reverseWords(self, s: str) -> str:
    split = s.split()
    result = ""
    for word in split:
      listed_word = list(word)
      self.reverseString(listed_word)
      result += "".join(listed_word) + " "
    result = result[:-1]
    return result

# another solution
class Solution_2:
  def reverseWords(self, s: str) -> str:
    result = ""
    n = len(s)
    left = 0
    right = 0
    while right < n:
      if s[right] == " ":
        result += s[left:right + 1][::-1]
        right += 1
        left = right
      else:
        right += 1
    result += " "
    result += s[left:right + 2][::-1]
    result = result[1:]
    return result

def check_result(result, expected_result):
  n = len(result)
  for i in range(n):
    assert result[i] == expected_result[i]

def example_1():
  s = "Let's take LeetCode contest"
  expected_result = "s'teL ekat edoCteeL tsetnoc"
  solution_handler = Solution_1
  result = solution_handler.reverseWords(solution_handler, s)
  check_result(result, expected_result)
  print("The result for example 1 is: " + result)

def example_2():
  s = "God Ding"
  expected_result = "doG gniD"
  solution_handler = Solution_1
  result = solution_handler.reverseWords(solution_handler, s)
  check_result(result, expected_result)
  print("The result for example 2 is: " + result)

example_1()
example_2()