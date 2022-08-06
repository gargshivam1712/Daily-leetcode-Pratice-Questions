class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_rec(arr , n , dp):

            if n <= 0:
                return 0

            if dp[n-1] == -1:
                dp[n-1] = max(arr[n-1] + rob_rec(arr , n - 2 , dp) , rob_rec(arr , n - 1  , dp))

            return dp[n-1]
        
        n = len(nums)
        dp = [-1] * n
        return rob_rec(nums , n , dp)
        
#         def rob_rec(arr , i , count , maximum ):
            
#             if i >= len(arr):
#                 maximum.append(count)
#                 return
                
#             rob_rec(arr , i + 2 , count + arr[i], maximum)
#             rob_rec(arr , i + 1 , count, maximum)
            
#         maximum = []
#         rob_rec(nums , 0 , 0, maximum)
        
#         return max(maximum)


    
        