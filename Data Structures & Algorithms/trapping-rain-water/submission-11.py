class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        p = []
        s = []

        p.append(0)
        s.append(0)

        for i in range(1, n-1): 
            p.append(max(height[0:i]))
            s.append(max(height[i+1:n]))

        p.append(0)
        s.append(0)

        total = 0

        for i in range(n):
            print(total, p[i], s[i], height[i])
            area_i = min(p[i],s[i]) - height[i]
            total += max(0, area_i)                 # area must not be negative

        return total
            


