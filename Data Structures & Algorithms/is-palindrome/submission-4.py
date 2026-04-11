class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        s = ''.join(char for char in s if char.isalnum()).lower() 
        n = len(s)

        j = 0
        k = n - 1

        while j < k:

            if s[j] == s[k]:
                
                j += 1
                k -= 1

            else:
                return False

        return True