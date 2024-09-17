def lps(input_string: str) -> int:
    def lps_helper(input_string: str, left: int, right: int) -> int:
        if left > right:
            return 0
        if input_string[left] == input_string[right]:
            return 2 + lps_helper(input_string, left + 1, right - 1)
        else:
            return max(lps_helper(input_string, left + 1, right), lps_helper(input_string, left, right - 1))

    return lps_helper(input_string, 0, len(input_string) - 1)