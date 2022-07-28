class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        
        start = 0
        end = 0
        maximum = 0

        zero_index = None
        count = 0
        print(arr)
        while end  < len(arr):
            if arr[end] == 0:
                count = count + 1
                if count > k :
                    maximum = max(maximum , end - start)
                    while start <= end :
                        if arr[start] == 0:
                            count = count - 1
                            start = start + 1
                            zero_index = start
                            break
                        start = start + 1


            print(arr[end] , start , end , maximum)
            end = end + 1
        maximum = max(maximum , end - start)
        return maximum