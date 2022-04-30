class Solution:
    @classmethod
    def isPalindrome(self, x: int) -> bool:
        return True if str(x) == "".join(reversed(str(x))) else False
    
        
print(Solution.isPalindrome(123))