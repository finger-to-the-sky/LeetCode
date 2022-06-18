# Самая длинная палиндромная строка

class Solution:

    def palin_max(self, string):
        result = {string[i:j]
                      for i in range(len(string))
                      for j in range(len(string))
                      if len(string[i:j]) >= 2 and
                      string[i:j][::-1] == string[i:j]
                      }
        return max(result, key=len)


s = Solution()
print(s.palin_max('abbadeffedpp'))