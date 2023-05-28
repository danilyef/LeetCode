'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.


'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        check_word = strs[0]
        
        done = False
        while not done:       
            for string in strs:
                if len(check_word) < 1:
                    return ""

                if not string.startswith(check_word):
                    check_word = check_word[:-1]
                    done = False
                    break
                    
                else:
                    done = True
                    
        return check_word
                