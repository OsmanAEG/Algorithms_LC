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

# naive solution
class Solution_1:
  def middleNode(self, head: ListNode) -> ListNode:
    this_linked_list = LinkedList()
    this_linked_list.insert_node(head)
    length = this_linked_list.list_length()

    for i in range(length//2):
      head = head.next

    return head

# efficient and simple solution
class Solution_2:
  def middleNode(self, head: ListNode) -> ListNode:
    tmp_skip2 = head
    while tmp_skip2 and tmp_skip2.next:
      head = head.next
      tmp_skip2 = tmp_skip2.next.next
    return head

# check results
def check_result(result, expected_result):
  assert result == expected_result

def example_1():
  first_node = ListNode(1)
  this_linked_list = LinkedList()
  this_linked_list.insert_node(first_node)

  for i in range(2, 6):
    next_node = ListNode(i)
    this_linked_list.insert_node(next_node)

  expected_result = 3
  solution_handler = Solution_2
  result = solution_handler.middleNode(solution_handler, first_node)
  check_result(result.val, expected_result)
  print("The result for example 1 is: " + str(result.val))

def example_2():
  first_node = ListNode(1)
  this_linked_list = LinkedList()
  this_linked_list.insert_node(first_node)

  for i in range(2, 7):
    next_node = ListNode(i)
    this_linked_list.insert_node(next_node)

  expected_result = 4
  solution_handler = Solution_2
  result = solution_handler.middleNode(solution_handler, first_node)
  check_result(result.val, expected_result)
  print("The result for example 2 is: " + str(result.val))

example_1()
example_2()
