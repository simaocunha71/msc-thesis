        List<Integer> result = new ArrayList<>();
        int current_sum = 0;
        int current_factorial = 1;

        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                result.add(current_factorial);
                current_factorial *= i;
            } else {
                current_sum += i;
                result.add(current_sum);
            }
        }

        return result;
    }
}

