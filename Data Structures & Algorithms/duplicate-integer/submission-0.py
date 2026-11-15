class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

    #  The brute force solution would be to check every element against the other and will be too slow 

    #the solution will be to implement an hashmap, hmm, i think a set will be better this case, then i will load up the set. if the everything enters the set without any falsy response, it is good. but if its falsy or an exception it should return true


#Gaps, how can i create a set and use it methods. figured
        s = set()
        for i in nums:
            if i in s:
                return True
            
            s.add(i)
            
        return False
        
    


     

        