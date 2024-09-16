"""
def is_samepatterns(arr, patterns):
    if not arr or not patterns:
        return False
    for i in range(len(arr)):
        if not patterns[i % len(patterns)] == arr[i]:
            return False
    return True
"""
