        if (n == 0) {
            return 1;
        }
        int res = modp(n / 2, p);
        res *= res;
        res %= p;
        if (n % 2 == 1) {
            res *= n;
        }
        return res % p;
    }
    public boolean isSubsetSum(int set[], int n, int sum) {
        boolean subset[][] = new boolean[n + 1][sum + 1];

        // If sum is 0, then answer is true
        for (int i = 0; i <= n; i++) {
            subset[i][0] = true;
        }

        // If sum is not 0 and set is empty, then
        // answer is false
        for (int i = 1; i <= sum; i++) {
            subset[0][i] = false;
        }

        // Fill the subset table in botton up manner
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= sum; j++) {
                if (j < set[i - 1]) {
                    subset[i][j] = subset[i - 1][j];
                }
                else {
                    subset[i][j] = subset[i - 1][j]
                            || subset[i - 1][j - set[i - 1]];
                }
            }
        }

        /* uncomment this code to print table*/
        // for (int i = 0; i <= n; i++) {
        // for (int j = 0; j <= sum; j++) {
        // System.out.print(subset[i][j] + " ");
        // }
        // System.out.println();
        // }
        return subset[n][sum];
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.isSubsetSum(new int[]{3, 4, 5, 6, 7, 8, 9}, 7, 