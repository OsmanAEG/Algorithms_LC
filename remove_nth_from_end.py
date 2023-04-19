class ListNode:
  def __init__(self, val = 0, next=None):
    self.val = val
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_node(self, next_node: ListNode):
    if(self.head):
      current_node = self.head

      while(current_node.next):
        current_node = current_node.next

      current_node.next = next_node

    else:
      self.head = next_node

  def output_list(self):
    output_node = self.head

    while(output_node):
      print(output_node.val)
      output_node = output_node.next

  def list_length(self):
    current_node = self.head
    length = 0

    while(current_node):
      length += 1
      current_node = current_node.next

    return length

# check results
def check_result(result, expected_result):
  i = 0

  while(result):
    assert result.val == expected_result[i]
    result = result.next
    i += 1

# alternative solution
class Solution_2:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    

def example_1():
  first_node = ListNode(1)
  this_linked_list = LinkedList()
  this_linked_list.insert_node(first_node)

  for i in range(2, 6):
    next_node = ListNode(i)
    this_linked_list.insert_node(next_node)

  n = 2

  expected_result = [1, 2, 3, 5]
  solution_handler = Solution_1
  result = solution_handler.removeNthFromEnd(solution_handler, first_node, n)

  check_result(result, expected_result)
  print("Results to example 1 are successful!")

def example_2():
  first_node = ListNode(1)
  this_linked_list = LinkedList()
  this_linked_list.insert_node(first_node)

  n = 1

  expected_result = []
  solution_handler = Solution_1
  result = solution_handler.removeNthFromEnd(solution_handler, first_node, n)

  check_result(result, expected_result)
  print("Results to example 2 are successful!")

def example_3():
  first_node = ListNode(1)
  this_linked_list = LinkedList()
  this_linked_list.insert_node(first_node)

  for i in range(2, 3):
    next_node = ListNode(i)
    this_linked_list.insert_node(next_node)

  n = 1

  expected_result = [1]
  solution_handler = Solution_1
  result = solution_handler.removeNthFromEnd(solution_handler, first_node, n)

  check_result(result, expected_result)
  print("Results to example 3 are successful!")

example_1()
example_2()
example_3()