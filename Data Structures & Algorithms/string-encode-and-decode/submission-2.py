class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for i in strs:
            encode+=str(len(i))+"#"+i
        return encode
        pass


    def decode(self, s: str) -> List[str]:
        res,i = [],0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            lenght = int(s[i:j])
            res.append(s[j+1:j+1+lenght])
            i = j+1+lenght
        return res

        pass
