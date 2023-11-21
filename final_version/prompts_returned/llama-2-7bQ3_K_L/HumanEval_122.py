
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    
    # Write your code here
    ans = []
    s = sum(arr[:k]) if arr[k-1] >= 10**4 else sum(arr[:k-1]) + (arr[k-1]+1)*2**3
    if arr[-1]>=10**4:
        ans.append((s,int(10*sum(arr[:k-1]))))
    
    for i in range(len(arr)):
        #print("{}".format(arr[i]))
        s+=int(10*(arr[i]+arr[i+1])) if arr[i]>=10**4 else int(10*arr[i])
        ans.append((s,int(10*(arr[-1]+arr[len(arr)-2]))) if arr[i]+arr[len(arr)-2] >= 10**4 else (s+1)*2)
    return max(ans, key = lambda x: -x[1])
        
