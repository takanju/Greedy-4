
# Problem2:  Equal Row From Minimum Domino Rotations
# https: // leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        TC:O(n)
        SC:O(n)
        """
        mapp = {}
        maxfreq = 0
        maxx = 0
        for i in range(0, len(tops)):
            count = 0
            if tops[i] in mapp:
                mapp[tops[i]] += 1
                count = mapp[tops[i]]
                if count >= len(tops):
                    maxx = tops[i]
                    break
            else:
                mapp[tops[i]] = 1

            if bottoms[i] in mapp:
                mapp[bottoms[i]] += 1
                count = mapp[bottoms[i]]
                if count >= len(bottoms):
                    maxx = bottoms[i]
                    break
            else:
                mapp[bottoms[i]] = 1

        print(mapp)
        print(count)

        arot, brot = 0, 0
        for i in range(0, len(tops)):
            if tops[i] != maxx and bottoms[i] != maxx:
                return -1
            elif bottoms[i] != maxx:
                brot += 1
            elif tops[i] != maxx:
                arot += 1
        return min(arot, brot)
