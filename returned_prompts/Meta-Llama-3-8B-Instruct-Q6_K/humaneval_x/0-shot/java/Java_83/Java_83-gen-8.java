        int count = 0;
        for (int i = 1; i < 10; i++) {
            for (int j = 0; j < n; j++) {
                int num = i * (int) Math.pow(10, j) + i * (int) Math.pow(10, n - 1);
                if (num > 0 && (num % 10 == 1 || num / (int) Math.pow(10, n - 1) % 10 == 1)) {
                    count++;
                }
            }
        }
        return count;
    }
}
// https://leetcode.com/problems/numbers-with-speci
// fied-one-digits-and-digit-sum
// https://leetcode.com/problems/numbers-with-specific-one-digits-and-digit-sum/

