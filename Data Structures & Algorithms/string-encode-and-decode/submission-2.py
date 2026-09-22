class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)) + "#" + word)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)
        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])     
            j += 1                   
            word = s[j:j + length]   
            res.append(word)
            i = j + length    
        return res
