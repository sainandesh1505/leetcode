class Solution:
    def longestCommonPrefix(self, strs):
        
        prefix = strs[0]

        for word in strs[1:]:

            while word.startswith(prefix) == False:
                prefix = prefix[:-1]

            if prefix == "":
                return ""

        return prefix
