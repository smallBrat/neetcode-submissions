class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        new_s1 = sorted(s)
        new_s2 = sorted(t)

        if new_s1==new_s2:
            return True
        
        return False