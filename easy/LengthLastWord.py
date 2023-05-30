'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 
Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.


'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = len(s.strip().split()[-1])
        return s
    



class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # base case
        if len(s) == 1 and s != ' ':
            return 1
        
        i = len(s) - 1
        len_word = 0
        while True:

            if s[i] == ' ':
                i -= 1
                
            elif s[i] != ' ' and (s[i-1] == ' ' or i == 0):
                len_word +=1
                return len_word
            
            elif s[i] != ' ' and s[i-1] != ' ':
                i -= 1
                len_word +=1