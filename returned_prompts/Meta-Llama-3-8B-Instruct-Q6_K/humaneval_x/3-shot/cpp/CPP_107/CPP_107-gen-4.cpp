    vector<int> result(2);
    for(int i = 1; i <= n; i++) {
        string str = to_string(i);
        if (str == string(str.rbegin(), str.rend())) {
            if (i % 2 == 0) {
                result[0]++;
            } else {
                result[1]++;
            }
        }
    }
    return result;
}
// This function counts the number of even and odd palindromes within the given range
// It does this by converting each integer to a string, checking if it's a palindrome
// If it is, it increments the corresponding count in the result vector
// The result vector is returned at the end
// Time complexity: O(n)
// Space complexity: O(1)
// This function assumes that n is a positive integer
// This function assumes that the input is valid (1 <= n <= 10^3) and the output is valid (vector of two integers)