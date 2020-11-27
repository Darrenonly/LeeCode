class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        题目：
        构造一个函数，得到字符串中不重复的最大字串长度
        input type s: str
        output type : int
        """
        der = {}
        index_start, ans = 0, 0
        for index_end in range(len(s)):
            if s[index_end] in der:
                index_start = max(der[s[index_end]], index_start)
            ans = max(ans, index_end - index_start + 1)
            der[s[index_end]] = index_end + 1
        return ans


if __name__ == "__main__":
    test_str = ["abcabcdef", "pwwkew", " ", "bbbbbbb", "dvdg"]
    sol = Solution()
    for s in test_str:
        length = sol.lengthOfLongestSubstring(s)
        print(length)
