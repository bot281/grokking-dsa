class Solution:
    def containsDuplicate(self, nums):
      # TODO: Write your code here
      temp = []
      for n in nums:
        if n in temp:
           return True
        else:
           temp.append(n)
      return False

if __name__ == "__main__":
   sample1 = [1,2,3,4]
   sample2 = [1,2,3,1]
   sample3 = [3,2,6,-1,2,1]

   solution = Solution()
   print(solution.containsDuplicate(sample1))
   print(solution.containsDuplicate(sample2))
   print(solution.containsDuplicate(sample3))