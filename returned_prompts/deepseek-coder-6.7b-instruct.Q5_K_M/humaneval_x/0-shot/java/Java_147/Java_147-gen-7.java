        int count = 0;
        int[] arr = new int[n+1];
        for (int i = 1; i <= n; i++) {
            arr[i] = i*i - i + 1;
        }

        for (int i = 1; i <= n-2; i++) {
            for (int j = i+1; j <= n-1; j++) {
                for (int k = j+1; k <= n; k++) {
                    if ((arr[i] + arr[j] + arr[k]) % 3 == 0) {
                        count++;
                    }
                }
            }
        }
        return count;
    }

    public static void main (String[] args) {
        // keep this function to test your code
        Solution sol = new Solution();
        int n = 5;
        System.out.println(sol.getMaxTriples(n));
    }
}

// Time complexity of this solution is O(n^3) and space complexity is O(n).
// This solution can be improved to O(n^2) by using a hashmap to store the frequency of each remainder when divided by 3.

// This solution is not optimal because it has a time complexity of O(n^3). 
// This is because it has to calculate the sum of every combination of three numbers, which is O(n^3).
// However, the problem statement does not specify a time limit, so this solution is acceptable.

// If the problem was to find the number of triples such that the sum was a multiple of 3, then we could use a hashmap to store the counts of each remainder when divided by 3, and then use these counts to calculate the number of triples. This would reduce the time complexity to O(n^2).

// The space complexity is O(n) because we are storing an array of size n.

// The code is written in Java and uses three nested loops to find all possible combinations of three numbers. For each combination, it checks if the sum is a multiple of 3 and if so, it increments the count. Finally, it returns the count.

// The main function is used to test the code by creating an object