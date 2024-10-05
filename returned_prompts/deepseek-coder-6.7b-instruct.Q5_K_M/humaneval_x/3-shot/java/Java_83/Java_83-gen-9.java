        if (n < 1) return 0;

        int count = 0;
        for(int i = 1; i <= n; i++) {
            if (i == 1 || i == n) {
                count += 9 * Math.pow(10, n - 1);
            } else {
                count += 9 * Math.pow(10, n - i);
            }
        }

        return count;
     }
 }

