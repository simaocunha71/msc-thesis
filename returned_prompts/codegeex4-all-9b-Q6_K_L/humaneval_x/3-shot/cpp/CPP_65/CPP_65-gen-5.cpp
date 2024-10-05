
Here is my review of each function:

has_close_elements:

The algorithm is correct, but it is not efficient.  If the vector is sorted, then you can find the minimum difference between any two elements in O(n) time, instead of O(n^2) time.  You can do this by iterating through the vector, keeping track of the minimum difference seen so far, and the two elements that produced that minimum difference.  If you find a difference between two elements that is smaller than the minimum difference seen so far, then you update the minimum difference and the two elements that produced that minimum difference.  At the end, if the minimum difference is less than the threshold, then you return true, otherwise you return false.

separate_paren_groups:

The algorithm is correct, but it is not efficient.  If the string is well-formed, then you can find the start and end indices of each group in O(n) time, instead of O(n^2) time.  You can do this by iterating through