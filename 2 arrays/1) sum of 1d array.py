# given 1-d array of int
# create new array representing sum of original array
# running sum at pos i in new array calculated as sum of all nums in original array from 0th index up to i-th index (inclusive)
# resulting array computed as --> result [i] = sum(nums[0] + nums[1] + ... + nums[i]) for each i from 0 to length of array minus one

# example:
# input: [2,3,5,1,6]
# expect output: [2,5,10,11,17]

class Solution:
    def runningSum(self, nums):
        result = [0] * len(nums)
        # TODO: Write your code here
        # [0,0,0,0,0]
        for i, n in enumerate(nums):
            if result[0] != nums[0]:
                result[0] = nums[0]
            else:
                result[i] = result[i] + n + result[i-1]


        ###

        return result
    
if __name__ == "__main__":
    test = [3,1,4,2,2]
    print(Solution().runningSum(test)) # [3,4,8,10,12]
