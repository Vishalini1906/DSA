class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        arr = sorted((x, i) for i, x in enumerate(nums))
        ans = [0] * n

        i = 0

        while i < n:
            j = i + 1

            while j < n and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1

            indices = sorted(arr[k][1] for k in range(i, j))

            for k in range(i, j):
                ans[indices[k - i]] = arr[k][0]

            i = j

        return ans
        