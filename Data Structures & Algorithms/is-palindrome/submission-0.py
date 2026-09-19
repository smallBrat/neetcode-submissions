class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        n = len(s)
        i = 0
        j = n - 1

        while i < j:
            if s[i].isalnum() != True:
                i += 1
            elif s[j].isalnum() != True:
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1

        return True