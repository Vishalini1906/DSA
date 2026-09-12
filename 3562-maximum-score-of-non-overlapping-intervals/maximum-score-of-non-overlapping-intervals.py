from functools import lru_cache
from bisect import bisect_right
from math import inf

class Solution:
    def maximumWeight(self, intervals):
        intervals = sorted((*x, i) for i, x in enumerate(intervals))
        starts = [x[0] for x in intervals]

        @lru_cache(None)
        def dp(i, k):
            if i == len(intervals) or k == 0:
                return (0, ())

            skip = dp(i + 1, k)

            l, r, w, idx = intervals[i]
            j = bisect_right(starts, r)

            nxt = dp(j, k - 1)
            take = (w + nxt[0], tuple(sorted((idx,) + nxt[1])))

            if take[0] > skip[0]:
                return take
            if take[0] < skip[0]:
                return skip

            return min(take, skip, key=lambda x: x[1])

        return list(dp(0, 4)[1])
        