        // sort by sum of digits
        Collections.sort(nums, new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                int sum_a = sumDigits(a);
                int sum_b = sumDigits(b);
                if (sum_a != sum_b) return Integer.compare(sum_a, sum_b);
                else return Integer.compare(a, b);
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

