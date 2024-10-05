        if (n <= 0) {
            return false;
        }
        for (int i = 2; i <= n; i += 2) {
            if (n - i <= 0) {
                return true;
            }
            for (int j = 2; j <= n - i; j += 2) {
                if (n - i - j <= 0) {
                    return true;
                }
                for (int k = 2; k <= n - i - j; k += 2) {
                    if (n - i - j - k <= 0) {
                        return true;
                    }
                    for (int l = 2; l <= n - i - j - k; l += 2) {
                        if (n - i - j - k - l == 0) {
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }
}

// Time complexity O(n^4)
// Space complexity O(1)

Explanation:
The problem asks whether the given number n can be written as the sum of exactly 4 positive even numbers. The solution checks all possible combinations of 4 even numbers from 2 to n. If any combination sums up to n, the function returns true. If no combination is found, the function returns false.

The time complexity of the solution is O(n^4), where n is the input number. This is because there are four nested loops, each iterating from 2 to n. The space complexity is O(1), as only a constant amount of space is used to store the variables.