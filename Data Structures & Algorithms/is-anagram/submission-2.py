class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #first whats an anagram?
        #two words are anagrams of each other if they contain exactly same characters.


        # this approach is fast but it consumes memory





        #check size
        if len(s) != len(t):
            return False
        
        # if ''.join(sorted(s)) != ''.join(sorted(t)):
        #     return False
        # else:
        #     return True




        count = {}


        for c in s:
            count[c] = count.get(c, 0) + 1
        for c in t:
            count[c] = count.get(c, 0) - 1
            if count[c] < 0:
                return False
        return True

            

        


        

        
