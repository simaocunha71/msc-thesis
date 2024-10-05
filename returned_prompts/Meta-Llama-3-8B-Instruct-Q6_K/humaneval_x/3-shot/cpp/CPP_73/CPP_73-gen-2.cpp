    int n = arr.size();
    int res = 0;
    int left = 0, right = n - 1;
    while (left < right) {
        if (arr[left] == arr[right]) {
            left++;
            right--;
        } else {
            res++;
            left++;
        }
    }
    return res;
} // O(n) time complexity


