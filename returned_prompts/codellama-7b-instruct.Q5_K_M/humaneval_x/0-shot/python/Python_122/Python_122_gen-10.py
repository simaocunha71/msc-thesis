
def add_elements(arr, k):
    count = 0
    for i in range(k):
        if len(str(arr[i])) == 2:
            count += arr[i]
    return count

# EOF
