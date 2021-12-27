class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in range(len(strs)):
            x= ''.join(sorted(strs[i]))
            if x not in anagrams:
                anagrams[x]=[strs[i]]
            else:
                anagrams[x].append(strs[i])
        return anagrams.values()