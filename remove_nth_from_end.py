class ListNode:
  def __init__(self, val = 0, next=None):
    self.val = val
    self.next = next

class solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    k = len(head)
    k_del = k-n
    

def example_1():
  head = [1, 2, 3, 4, 5]
  n = 2
  expected_result = [1, 2, 3, 5]

def example_2():
  head = [1]
  n = 1
  expected_result = []

def example_3():
  head = [1, 2]
  n = 1
  expected_result = [1]