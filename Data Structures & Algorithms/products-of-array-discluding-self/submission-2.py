class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # num only has 41 possible values
                
        # nums  = [-1,  0,  1,  2,  3]
        # p     = [ 1, -1,  0,  0,  0]
        # s     = [ 0,  6,  6,  3,  1]
        # r     = [ 0, -6,  0,  0,  0]

        p_arr = [1] * len(nums)
        s_arr = [1] * len(nums)
        r_arr = [1] * len(nums)

        p = 1
        s = 1

        for i in range(len(nums)):
            p_arr[i] = p
            p = p * nums[i]

        for j in range(len(nums) -1, -1, -1):
            s_arr[j] = s
            s = s * nums[j]

            r_arr[j] = p_arr[j] * s_arr[j]

        return r_arr

        

            
            





