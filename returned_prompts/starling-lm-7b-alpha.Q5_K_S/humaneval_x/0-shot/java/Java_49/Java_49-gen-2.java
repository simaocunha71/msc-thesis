        if (n == 0) {
            return 1;
        }
        if (n % 2 == 0) {
            int a = modp(n / 2, p);
            return (int) (((long) a * a) % p);
        } else {
            int a = modp(n - 1, p);
            return (int) (((long) a * n) % p);
        }
    }

    public int[] productExceptSelf(int[] nums) {
        int[] left = new int[nums.length];
        left[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            left[i] = nums[i - 1] * left[i - 1];
        }

        int[] right = new int[nums.length];
        right[nums.length - 1] = 1;
        for (int i = nums.length - 2; i >= 0; i--) {
            right[i] = nums[i + 1] * right[i + 1];
        }
        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                res[i] = 0;
            } else {
                res[i] = left[i] * right[i];
            }
        }
        return res;
    }

    public int maximumPopulation(int[] y, int[] x, int[] d) {
        int maxYear = 0;
        int[] yCount = new int[101];
        for (int i = 0; i < y.length; i++) {
            int year = y[i];
            yCount[year]++;
            maxYear = Math.max(maxYear, year);
        }
        int[] maxYears = new int[maxYear + 1];
        for (int i = 0; i < d.length; i++) {
            int year = y[i];
            int