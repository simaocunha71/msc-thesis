        List<Integer> result = new ArrayList<>();
        int current_divisor = 2;

        while (n > 1) {
            if (n % current_divisor == 0) {
                result.add(current_divisor);
                n /= current_divisor;
            } else {
                current_divisor += 1;
            }
        }
        return result;
    }
}

