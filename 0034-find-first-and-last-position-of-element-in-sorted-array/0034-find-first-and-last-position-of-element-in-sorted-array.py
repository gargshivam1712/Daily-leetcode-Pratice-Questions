class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1,-1]
        low = 0
        high = n - 1
        left = None
        if nums[0] == target:
            left = 0
        else:
            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    if not nums[mid-1] == target:
                        left = mid
                        break
                    else:
                        high = mid - 1

                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1

            if left == None:
                return [-1 , -1]

        low = 0
        high = n -1
        right = None
        if nums[high] == target:
            right = high
        else:
            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    if not nums[mid+1] == target:
                        right = mid
                        break
                    else:
                        low = mid + 1

                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1

        return [left , right]
