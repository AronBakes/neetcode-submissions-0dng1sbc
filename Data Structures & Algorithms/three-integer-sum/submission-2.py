class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        nums.sort()        
        n = len(nums)

        for i in range(n):
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]

            j = i + 1
            k = n - 1

            while j < k:

                current_sum = nums[j] + nums[k]

                if current_sum == target:
                    output.append([nums[i],nums[j],nums[k]])

                    # Skip duplicates for j (move forward)
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                        
                    # Skip duplicates for k (move backward)
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif current_sum < target:
                    j +=1
                else:
                    k -= 1

        return output