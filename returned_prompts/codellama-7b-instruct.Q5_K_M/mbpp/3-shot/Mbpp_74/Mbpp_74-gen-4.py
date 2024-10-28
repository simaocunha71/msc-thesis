
def is_samepatterns(patterns, arr):
    for i in range(len(arr)):
        if arr[i] != patterns[i % len(patterns)]:
            return False
    return True


