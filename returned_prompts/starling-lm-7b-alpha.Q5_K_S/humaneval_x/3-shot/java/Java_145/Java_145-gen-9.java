        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < nums.size(); i++) {
            result.add(nums.get(i));
        }
        result.sort((a, b) -> {
            int a_sum = sumOfDigits(a);
            int b_sum = sumOfDigits(b);

            if (a_sum == b_sum) {
                return Integer.compare(a, b);
            }
            return Integer.compare(a_sum, b_sum);
        });
        return result;
    }

    private int sumOfDigits(int num) {
        int sum = 0;
        while (num != 0) {
            sum += (num % 10);
            num /= 10;
        }
        return sum;
    }
}

