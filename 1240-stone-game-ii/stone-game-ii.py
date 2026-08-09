class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dp(i, M):
            if i >= n:
                return 0

            if i + 2 * M >= n:
                return suffix[i]

            if (i, M) in memo:
                return memo[(i, M)]

            best = 0

            for X in range(1, 2 * M + 1):
                new_M = max(M, X)
                opponent = dp(i + X, new_M)
                current = suffix[i] - opponent
                best = max(best, current)

            memo[(i, M)] = best

            return best

        return dp(0, 1)
        