    def longest_palindrome(string: str) -> str:
        result = ""
        for idx in range(len(string)):
            if len(string) - idx > result:
                if string[idx] == string[len(string) - idx - 1]:
                    curr_pal = string[idx:len(string) - idx]
                    if len(curr_pal) > len(result):
                        result = curr_pal
        return result

    def make_palindrome(string: str) -> str:
        prefix = string[:len(string) - len(longest_palindrome(string))]
        postfix = longest_palindrome(string)
        return prefix + postfix + prefix[::-1]


