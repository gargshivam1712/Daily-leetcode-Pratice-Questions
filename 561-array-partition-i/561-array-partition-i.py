class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        print(nums)
        total = 0
        for i in range(0,len(nums) , 2):
            total = total + nums[i+1]
            
        return total
            
        