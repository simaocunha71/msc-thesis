        List<Integer> result = new ArrayList<>();
        int current_factorial = 1;
        int current_sum = 0;

        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                current_factorial *= i;
                result.add(current_factorial);
            } else {
                current_sum += i;
                result.add(current_sum);
            }
        }
        return result;
    }
}

