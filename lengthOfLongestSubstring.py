class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        题目：
        构造一个函数，得到字符串中不重复的最大字串长度
        input type s: str
        output type : int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
            print(st)
        return ans


if __name__ == "__main__":
    test1 = 'abcabcdef'
    test2 = "pwwkew"
    test3 = " "
    test4 = "bbbbbbb"
    test5 = "dvdg"
    """
    commit test
    
    """

    sol = Solution()
    length = sol.lengthOfLongestSubstring(test2)
    print(length)
