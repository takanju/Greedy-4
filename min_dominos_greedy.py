
# Problem2:  Equal Row From Minimum Domino Rotations
# https: // leetcode.com/problems/minimum-domino-rotations-for-equal-row/
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        TC:O(n)
        SC:O(1)
        """
        res = self.check(tops, bottoms, tops[0])
        if res != -1:
            return res
        return self.check(tops, bottoms, bottoms[0])

    def check(self, tops, bottoms, target):
        arot = 0
        brot = 0
        for i in range(0, len(tops)):
            if tops[i] != target and bottoms[i] != target:
                return -1
            if tops[i] != target:
                arot += 1
            if bottoms[i] != target:
                brot += 1
        return min(arot, brot)
