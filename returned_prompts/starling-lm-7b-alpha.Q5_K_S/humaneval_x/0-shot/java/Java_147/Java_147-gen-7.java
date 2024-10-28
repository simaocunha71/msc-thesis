        int count = 0;

        int[] a = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            a[i] = (i * i) - i + 1;
        }

        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                for (int k = j + 1; k <= n; k++) {
                    int sum = a[i] + a[j] + a[k];

                    if (sum % 3 == 0) {
                        count++;
                    }
                }
            }
        }

        return count;
    }
}


    // Time Complexity : O(n^3)
    // Space Complexity : O(n)


    // Time Complexity : O(n^3)
    // Space Complexity : O(n)


    // Time Complexity : O(n^3)
    // Space Complexity : O(n)


    // Time Complexity : O(n^3)
    // Space Complexity : O(n)


    // Time Complexity : O(n^3)
    // Space Complexity : O(n)






































































































































































































