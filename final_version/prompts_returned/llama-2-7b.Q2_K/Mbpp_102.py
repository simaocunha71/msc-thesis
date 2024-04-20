"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""
class Solution:
    def snakeToCamel(self, snake_case_string: str) -> str:
        count = 0
        for char in reversed(snake_case_string):
            if char.isalnum():
                yield chr(ord(char)-1) + str(count)
            else:
                count += 1
            # yield char + count * "1" - count
        return ""
