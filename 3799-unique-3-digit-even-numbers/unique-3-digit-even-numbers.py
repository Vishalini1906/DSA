class Solution:
    def totalNumbers(self, digits):
        ans = set()
        n = len(digits)

        for i in range(n):
            if digits[i] % 2 != 0:
                continue

            for j in range(n):
                if j == i:
                    continue

                for k in range(n):
                    if k == i or k == j or digits[k] == 0:
                        continue

                    num = digits[k] * 100 + digits[j] * 10 + digits[i]
                    ans.add(num)

        return len(ans)
        