#class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         low = 0
#         high = len(nums)-1
#         mid = (low + high) //2
        
#         while mid >= low and mid <= high:
#             if(nums[mid] == target):
#                 return mid
#             if nums[mid] > target:
#                 high = mid-1
#                 mid = (low + high)//2
#             else:
#                 low = mid+1
#                 mid = (low + high)//2
            
#         return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) //2

            print(low , mid , high)

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1

        return -1
        
        # return self.searchRec(nums,0 , len(nums)-1 , target)
    
    # def searchRec(self , nums , low , high , target):
    #     mid = (low + high)//2
    #     if(mid >= low and mid <= high):
    #         if nums[mid]== target:
    #             return mid
    #         elif nums[mid] > target:
    #             return self.searchRec(nums , low , mid-1 , target)
    #         else:
    #             return self.searchRec(nums , mid + 1 , high , target)
    #     else:
    #         return -1

        