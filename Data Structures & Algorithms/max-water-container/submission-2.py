class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        j = 0
        k = n - 1

        best_area = 0

        while j < k:

            w = k - j
            h = min(heights[j], heights[k])
            a = w * h

            # print(w,h,a, j, heights[j], k, heights[k])

            if a > best_area:
                best_area = a

            if heights[j] < heights[k]:
                j += 1
            elif heights[j] > heights[k]:
                k -= 1
            else:
                j += 1
                k -= 1
            
        return best_area

            
