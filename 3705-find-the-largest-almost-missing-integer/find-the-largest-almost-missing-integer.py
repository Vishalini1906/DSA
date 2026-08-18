from collections import Counter

class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)

        if k == 1:
            count = Counter(nums)
            ans = -1

            for num in count:
                if count[num] == 1:
                    ans = max(ans, num)

            return ans

        if k == n:
            return max(nums)

        ans = -1

        if nums.count(nums[0]) == 1:
            ans = max(ans, nums[0])

        if nums.count(nums[-1]) == 1:
            ans = max(ans, nums[-1])

        return ans
        