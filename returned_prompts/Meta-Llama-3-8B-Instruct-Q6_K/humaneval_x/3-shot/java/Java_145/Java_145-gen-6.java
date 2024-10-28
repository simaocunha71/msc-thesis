        Collections.sort(nums, (a, b) -> {
            int sumA = sumDigits(a);
            int sumB = sumDigits(b);
            if (sumA == sumB) {
                return Integer.compare(nums.indexOf(a), nums.indexOf(b));
            } else {
                return Integer.compare(sumA, sumB);
            }
        });
        return nums;
    }

    private int sumDigits(int n) {
        int sum = 0;
        while (n != 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
}

