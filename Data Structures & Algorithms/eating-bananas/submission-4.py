class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # k = #
        max_value = max(piles)
        total = sum(piles)
        n = len(piles)

        if h == n: 
            return max_value

        if h >= total:
            return 1

        def canEatAll(piles: List[int], k: int, h: int) -> bool:
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k     # This replaces math.ceil(pile / k)
                
                if hours > h:
                    return False
            
            return hours <= h

        k_upper = max_value
        k_lower = 1

        while k_lower <= k_upper:

            k = k_lower + (k_upper - k_lower) // 2
            eatCheck = canEatAll(piles, k, h)

            if eatCheck:
                k_upper = k - 1
            else:
                k_lower = k + 1

        return k_lower







