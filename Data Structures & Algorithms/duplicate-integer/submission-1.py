class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        beenHere = set() 
        for i in nums:
            if i in beenHere: 
                return True
            beenHere.add(i) 
        return False         
        
        