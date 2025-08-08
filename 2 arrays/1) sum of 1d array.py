class Solution:
    def runningSum(self, nums):
        result = [0] * len(nums)  
        # TODO: Write your code here
        # [0, 0, 0, 0, 0]
        # [             ]
        for i, n in enumerate(nums):
            if result[0] != nums[0]:
                result[0] = nums[i]
            else:
                result[i] = result[i - 1] + n

        return result
    

if __name__ == "__main__":
    sample1 = [2, 3, 5, 1, 6]
    sample2 = [1, 1, 1, 1, 1]
    sample3 = [-1, 2, -3, 4, -5]

    print(Solution().runningSum(sample1))
    print(Solution().runningSum(sample2))
    print(Solution().runningSum(sample3))