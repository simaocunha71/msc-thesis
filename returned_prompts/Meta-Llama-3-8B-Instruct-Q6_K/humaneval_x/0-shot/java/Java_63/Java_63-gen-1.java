public class Solution {
    public int fibfib(int n) {
        if (n <= 1) {
            return 0;
        }
        if (n == 2) {
            return 1;
        }
        int a = 0, b = 0, c = 1, d = 1;
        for (int i = 3; i <= n; i++) {
            int temp = a + b + c;
            a = b;
            b = c;
            c = d;
            d = temp;
        }
        return d;
    }
}
The solution first checks if the input `n` is less than or equal to 1. If it is, the function returns 0 because the first two elements of the fibfib sequence are both 0. If `n` is 2, the function returns 1 because the third element of the fibfib sequence is 1.

Then, the function initializes four variables `a`, `b`, `c`, and `d` to the first four elements of the fibfib sequence: 0, 0, 1, and 1. It then enters a loop that runs `n-2` times. In each iteration of the loop, the function calculates the next element of the fibfib sequence by adding the last three elements together, and then updates the last three elements by shifting them one position to the left.

Finally, the function returns the last element of the fibfib sequence, which is stored in the variable `d`. This solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for large values of `n`.