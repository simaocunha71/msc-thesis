"""
Write a function to find maximum run of uppercase characters in the given string.
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
"""
# Time Complexity: O(n)
# Space Complexity: O(1), no additional space is used
def getMaxRunOfUppercases(str):
    # if len(str) <= 1: return str[0]
    count = {ord('a'): 0, ord('A'): 0}

    for i in range(len(str)):
        char = str[i]
        if ord(char.lower()) >= ord("a"): continue
        if ord(char.upper()) < ord("Z") or ord(char) == ord("z"):
            count["A"] += 1
        else:
            count["a"] += 1

    max_run = 0
    for key, value in count.items():
        if value > max_run:
            max_run = value
    return max_run

if __name__ == "__main__":
    

