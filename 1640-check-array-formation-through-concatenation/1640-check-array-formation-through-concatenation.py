class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        
        dic = {}
        
        for i in range(len(pieces)):
            dic[pieces[i][0]] = i
            
        start = 0
        
        temp_arr = None
        
        for i in range(len(arr)):
            
           
            
            if temp_arr == None:
                try:
                    
                    if dic[arr[i]]>=0 :
                        temp_arr = pieces[dic[arr[i]]]
                        start = start + 1
                        if len(temp_arr) == start:
                            temp_arr = None
                            start = 0
                            
                       
                        continue
                        
                except KeyError:
                    return False
                
            
                
            if arr[i] == temp_arr[start]:
                start = start + 1
                
            else:
                return False
            
            if len(temp_arr) == start:
                temp_arr = None
                start = 0
                
        return True
            
            
            