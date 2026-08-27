class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - 97] += 1

        ans = []
        pos = -1

        for i in range(len(target)):
            x = ord(target[i]) - 97

            if cnt[x] > 0:
                cnt[x] -= 1
                ans.append(target[i])
                pos = i
            else:
                for j in range(x + 1, 26):
                    if cnt[j] > 0:
                        cnt[j] -= 1
                        ans.append(chr(j + 97))

                        for k in range(26):
                            ans.extend([chr(k + 97)] * cnt[k])

                        return ''.join(ans)
                break

        if pos == -1:
            for j in range(ord(target[0]) - 96, 26):
                if cnt[j] > 0:
                    cnt[j] -= 1
                    result = [chr(j + 97)]

                    for k in range(26):
                        result.extend([chr(k + 97)] * cnt[k])

                    return ''.join(result)
            return ""

        while pos >= 0:
            x = ord(target[pos]) - 97
            cnt[x] += 1

            for j in range(x + 1, 26):
                if cnt[j] > 0:
                    cnt[j] -= 1

                    result = list(target[:pos])
                    result.append(chr(j + 97))

                    for k in range(26):
                        result.extend([chr(k + 97)] * cnt[k])

                    return ''.join(result)

            pos -= 1

        return ""
        