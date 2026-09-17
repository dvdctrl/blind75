class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappy = {} # val : index
        # i = index, n = actual number
        for i,n in enumerate (nums): 
                diff = target - n
                if diff in mappy:
                    return [mappy[diff], i]
                mappy[n]=i
                
                    
            
             
    