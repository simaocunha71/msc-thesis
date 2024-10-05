        List<Integer> result = new ArrayList<>();
        int current = 2;

        while (current * current <= n) {
            int count = 0;
            while (n % current == 0) {
                n /= current;
                count++;
            }
            if (count > 0) {
                for (int i = 0; i < count; i++) {
                    result.add(current);
                }
            }
            current++;
        }

        if (n > 1) {
            result.add(n);
        }
        return result;
    }
}

