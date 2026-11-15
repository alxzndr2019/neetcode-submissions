class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #first whats an anagram?
        #two words are anagrams of each other if they contain exactly same characters.





        #check size
        if len(s) != len(t):
            return False
        
        if ''.join(sorted(s)) != ''.join(sorted(t)):
            return False
        else:
            return True

        

        
        # sort and compare
