#leetcode 8 ATOI function
#Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0  # Return 0 for empty string
        
        i = 0
        ans = 0
        negative = 1
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        # Skip leading whitespaces
        while i < len(s) and s[i] == " ":
            i += 1
        
        # Check for sign
        if i < len(s) and (s[i] == "-" or s[i] == "+"):
            negative = -1 if s[i] == "-" else 1
            i += 1
        
        # Process numeric characters
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            if ans > (INT_MAX - digit) // 10:  # Check for overflow
                return INT_MAX if negative == 1 else INT_MIN
            ans = ans * 10 + digit
            i += 1
        
        return ans * negative
