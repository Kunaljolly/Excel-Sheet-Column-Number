class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        d = {x:k+1 for k,x in enumerate(ascii_uppercase)}
        c = 0
        p = len(columnTitle)-1
        for i in columnTitle:
            c += d[i]*(26**p)
            p -= 1

        return c
