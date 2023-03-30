class Solution(object):
    def firstBadVersion(self, n):
      min_val = 1
      max_val = n

      while min_val < max_val:
        mid_val = min_val + (max_val - min_val)//2
        
        

        