class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res= defaultdict(list)
        for word in strs:
            count = [0] * 26

            for i in word:
                index=ord(i)-ord("a")
                count[index] += 1

            key_find=tuple(count)
            res[key_find].append(word)
        
        return list(res.values())
    