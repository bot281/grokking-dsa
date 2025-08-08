class Solution:
    def runningSum(sum, nums):
        # check if array is none or has no elements and return an empty list if true
        if nums is None or len(nums) == 0:
            return []
        
        # init a list to store running sum
        result = [0] * len(nums)
        result[0] = nums[0]

        # look thru list starting from index 1, add prev sum to current element
        for i in range(1, len(nums)):
            result[i] = result[i-1] + nums[i]

        # return list containing running sum
        return result
    
if __name__ == "__main__":
    solution = Solution()

    # test case
    testInputs = [
        [2,3,5,1,6],
        [1,1,1,1,1],
        [-1,2,-3,4,-5]
    ]

    for input_arr in testInputs:
        output = solution.runningSum(input_arr)

        print(" ".join(map(str, output)))