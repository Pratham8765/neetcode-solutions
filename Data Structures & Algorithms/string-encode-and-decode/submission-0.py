class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
             res+=str(len(s))+"#"+s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
    
        while i < len(s):
            j = i
        # Move j forward until we find the delimiter '#'
            while s[j] != "#":
                j += 1
            
        # The number before '#' is the length of the string
            length = int(s[i:j])
        
        # Slice the actual word
            word = s[j + 1 : j + 1 + length]
            res.append(word)
        
        # Move i to the start of the next length prefix
            i = j + 1 + length
        
        return res