        // Sort by sum of digits
        Collections.sort(nums, new Comparator<Integer>() {
            public int compare(Integer a, Integer b) {
                int sum_a = sumDigits(a);
                int sum_b = sumDigits(b);

                if (sum_a == sum_b) {
                    // If same sum, order by index in original list
                    return nums.indexOf(a) - nums.indexOf(b);
                } else {
                    return sum_a - sum_b;
                }
            }
        });

        return nums;
    }

    public int sumDigits(int n) {
        // Find sum of digits
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
}

