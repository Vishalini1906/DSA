class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre_sum = 0
        ans = 0
        m = {0: 1}  
        for i in range(n):
           pre_sum += nums[i]
           if pre_sum - k in m:
               ans += m[pre_sum - k]
           m[pre_sum] = m.get(pre_sum, 0) + 1
      
        return ans


        