class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        
        n = len(nums)
        
        i = n -1
        count = 0
        
        while i >= 0:
            left = 0 
            right = i - 1
            target = nums[i]
            while left < right:
                val = nums[left] + nums[right]
                if val > target:
                    count = count + right - left
                    right = right - 1
                    
                else:
                    left = left + 1
                    
            i = i - 1
                    
        return count
        