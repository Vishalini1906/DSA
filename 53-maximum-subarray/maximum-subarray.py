class Solution(object):
    def maxSubArray(self, nums):
        CurSum=nums[0]
        maxSum=nums[0]
        for i in range(1,len(nums)):
            CurSum=max(CurSum+nums[i],nums[i])
            maxSum=max(maxSum,CurSum)
        return maxSum
        