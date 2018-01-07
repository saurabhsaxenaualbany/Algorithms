class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        num = 0
        for i in xrange(len(s)-1):
            if d[s[i]] < d[s[i+1]]:
                num -= d.get(s[i])
            else:
                num += d.get(s[i])
            print num
        return num + d[s[-1]]
