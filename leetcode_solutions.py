class Solution:
    def findContentChildren(self, g: List, s: List) -> int:
    # -- 455 Assign Cookies
    # -- Easy
    # -- sorting + greedy search
    # -- complexity:
    # --        time: O(nlogn + mlogm) (m+n)+(nlogn + mlogm)
    # --        space O(logn + logm) (logn + logm) + (k)
        g.sort()
        s.sort()
        count = 0
        i = 0
        j = 0
        n_g, n_s = len(g), len(s)
        while i < n_g and j < n_s:
            while j < n_s and g[i] > s[j]:
                j += 1
            if j < n_s:
                count += 1
            i += 1
            j += 1
        return count