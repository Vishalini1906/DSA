class Solution:
    def missingMultiple(self, nums, k):
        seen = set(nums)

        i = 1

        while True:
            multiple = k * i

            if multiple not in seen:
                return multiple

            i += 1
        