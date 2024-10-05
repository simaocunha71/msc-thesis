        List<Integer> result = new ArrayList<>();

        Collections.sort(nums, (a, b) -> {
            int sum_a = sumOfDigits(a);
            int sum_b = sumOfDigits(b);

            if (sum_a == sum_b) {
                return Integer.compare(a, b);
            }
            return Integer.compare(sum_a, sum_b);
        });

        return result;
    }

    public int sumOfDigits(int number) {
        String s = Integer.toString(number);
        int sum = 0;
        for (char c : s.toCharArray()) {
            sum += c - '0';
        }
        return sum;
    }
}

