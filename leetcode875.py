# @Problem :875. Koko Eating Bananas
# @Author :zliang
import math

class Solution(object):
    def minEatingSpeed(self, piles, H):
        # finish within H → return true → slow down
        def possible(K):
            tmp = sum((p-1) / K + 1 for p in piles)
            #print("tmp=",tmp)
            return tmp <= H

        minK, maxK = 1, max(piles)
        while minK < maxK:
            K = minK + (maxK - minK) // 2
            #speed up → serach in upper section → reset lowerbound
            if not possible(K):
                minK = K + 1
            #slow down → search in lower section → reset upperbound
            else:
                maxK = K
        return minK


if __name__ == '__main__':
    solu = Solution()
    piles, H = [30, 11, 23, 4, 20], 5
    print("minK=", solu.minEatingSpeed(piles, H))    
    piles, H = [3, 6, 7, 11], 8
    print("minK=", solu.minEatingSpeed(piles, H))
