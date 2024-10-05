        List<Integer> result = new ArrayList<>();
        List<Integer> copy = new ArrayList<>();
        for (int n : nums) {
            copy.add(n);
        }
        Collections.sort(copy, (a, b) -> {
            int a_sum = sumOfDigits(a);
            int b_sum = sumOfDigits(b);
            if (a_sum != b_sum) return a_sum - b_sum;
            return Integer.compare(a, b);
        });
        return copy;
    }

    private int sumOfDigits(int number) {
        int result = 0;
        while (number > 0) {
            result += (number % 10);
            number /= 10;
        }
        return result;
    }
}

