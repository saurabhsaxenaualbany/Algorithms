class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        u = repr(x)
        a = 0
        b = len(u) - 1
        if u[a] == '-':
            # a += 1
            return False
        while a < b:
            if u[a] != u[b]:
                return False
            a += 1
            b -= 1

        return True
