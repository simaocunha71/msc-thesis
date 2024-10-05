class Solution {
    public int sumToN(int n) {
        return n * (n + 1) / 2;
    }
}

This version of the function uses the formula for the sum of an arithmetic series, which is more efficient for large n. The formula is n * (n + 1) / 2.

This function works by calculating the sum of the first n numbers, which is n * (n + 1) / 2. The multiplication is the sum of the first n numbers, and the division by 2 is to reduce the sum by half because we are including both positive and negative numbers.

For example, if n = 10, the function returns 55. If n = 1, the function returns 1.

This version of the function is more efficient than the previous one for large n because it only requires a constant amount of time, regardless of the value of n. The previous version of the function, which uses a for loop, would take longer to compute for large n because it has to perform the addition operation n times.

In conclusion, this version of the function is more efficient and should be used whenever possible.


