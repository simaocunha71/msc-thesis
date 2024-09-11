"""
def max_run_uppercase(s):
    max_run = 0
    for i in range(len(s)):
        if s[i].isupper():
            current_run = 1
            while i + current_run < len(s) and s[i + current_run].isupper():
                current_run += 1
            max_run = max(max_run, current_run)
    return max_run

print