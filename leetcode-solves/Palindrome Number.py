class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Base condition
        if x < 0:
            return False
        t = x
        rev = 0
        while x > 0:
            dig = (x % 10)
            rev = (rev * 10) + dig
            x = x // 10
        if (t == rev):
            return True
        else:
            return False