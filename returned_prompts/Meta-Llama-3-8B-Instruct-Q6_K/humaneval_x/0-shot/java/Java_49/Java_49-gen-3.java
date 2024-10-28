public int modp(int n, int p) {
    if (n == 0) {
        return 1;
    }
    int res = modp(n / 2, p);
    if ((n & 1) == 1) {
        res = (res * res) % p;
    }
    return res;
}
Explanation:

This solution uses the property of modular arithmetic that `(a * b) % p = ((a % p) * (b % p)) % p`. We use this property to calculate the result of `2^n` modulo `p` recursively.

The base case of the recursion is when `n` is 0, in which case the result is 1.

For each recursive call, we divide `n` by 2 and calculate the result of `2^(n/2)` modulo `p`. If `n` is odd, we multiply the result by itself modulo `p`. This is because `2^(n+1) = (2^n) * 2` and `(a * b) % p = ((a % p) * (b % p)) % p`.

This solution has a time complexity of O(log n) and a space complexity of O(log n) due to the recursive call stack. It is also efficient in terms of memory usage because it only stores the current result and the previous result in the recursive call stack.

Note that the problem statement does not specify whether the result should be a positive integer or not. In this solution, we assume that the result should be a positive integer, so we use the modulo operator `%` to ensure that the result is within the range `[0, p)`.

Also, note that the problem statement does not specify whether the input `n` is non-negative or not. In this solution, we assume that the input `n` is non-negative, so we do not need to handle the case where `n` is negative. If the input `n` can be negative, we would need to handle this case separately.