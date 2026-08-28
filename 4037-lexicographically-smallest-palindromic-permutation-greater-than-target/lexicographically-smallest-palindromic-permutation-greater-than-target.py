class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - 97] += 1

        mid = ""

        for i in range(26):
            if cnt[i] % 2:
                if mid:
                    return ""
                mid = chr(i + 97)
                cnt[i] -= 1

        for i in range(26):
            cnt[i] //= 2

        half = n // 2

        for i in range(half, -1, -1):
            temp = cnt[:]

            for j in range(i):
                x = ord(target[j]) - 97
                temp[x] -= 1

            if any(x < 0 for x in temp):
                continue

            if i == half:
                left = target[:half]
                candidate = left + mid + left[::-1]

                if candidate > target:
                    return candidate

                continue

            x = ord(target[i]) - 97

            for c in range(x + 1, 26):
                if temp[c] <= 0:
                    continue

                temp[c] -= 1

                left = target[:i] + chr(c + 97)

                for j in range(26):
                    left += chr(j + 97) * temp[j]

                candidate = left + mid + left[::-1]

                if candidate > target:
                    return candidate

                temp[c] += 1

        return ""