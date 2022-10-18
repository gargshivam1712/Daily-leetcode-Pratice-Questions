class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         low = 0
#         high = n - 1
        
        
#         if nums[low]>target:
#             return low
#         elif nums[n-1]<target:
#             return n
        
#         while low <= high:
#             mid = (low + high)//2
#             if(nums[mid] == target):
#                 return mid
            
#             if high - low == 0:
#                 if nums[low] < target:
#                     return low + 1
#                 else:
#                     return low
#             if(nums[mid]>target):
#                 high = mid -1
#             else:
#                 low = mid + 1 
#         return low
            
        n = len(nums)

        low = 0
        high = n - 1
        while low <= high:
            if nums[low] > target:
                return low
            elif nums[high] < target:
                return high + 1

            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif low == high:
                if nums[mid] > target:
                    return mid
                else:
                    return mid + 1            
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1
