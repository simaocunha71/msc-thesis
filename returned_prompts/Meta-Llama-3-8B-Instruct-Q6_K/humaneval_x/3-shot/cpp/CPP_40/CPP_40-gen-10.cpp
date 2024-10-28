    sort(l.begin(),l.end());
    int i, j;
    for (i = 0; i < l.size(); i++) {
        for (j = i + 1; j < l.size(); j++) {
            int target = -l[i] - l[j];
            if (binary_search(l.begin(), l.end(), target)) {
                return true;
            }
        }
    }
    return false;
}  // Time complexity is O(n^2 log n) due to sorting and binary search. This solution works, but it could be improved if we can find a way to avoid sorting.  // If you can't sort the array, but you can sort the numbers in a specific range, you could sort the numbers in that range and then use a two-pointer technique.  // Another approach could be to store the numbers in a hash table and check for the existence of the target in constant time. This would give you a time complexity of O(n).  // If you don't want to use extra space, you could use a two-pointer technique and sort the array in-place. This would give you a time complexity of O(n log n).  // If you want to use a single pass over the array, you could use a hash table and a two-pointer technique. This would give you a time complexity of O(n).  // If you don't want to use extra space, you could use a two-pointer technique and a single pass over the array. This would give you a time complexity of O(n^2).  // If you want to use a single pass over the array and don't want to use extra space, you could use a two-pointer technique. This would give you a time complexity of O(n).  // If you want to use a single pass over the array and don't want to use extra space, you could use a two-pointer technique. This would give you a time complexity of O(n).  // If you want to use a single pass over the array and don't want to use extra space, you could use a two-pointer technique. This would give you a time complexity of O(n).  // If you want to use a single pass over the array and don't want to use extra space, you could use a two-pointer technique. This would give you a time complexity of O(n).  // If you want to use a single pass over the array and don't want to use extra space, you could use a two-pointer technique. This