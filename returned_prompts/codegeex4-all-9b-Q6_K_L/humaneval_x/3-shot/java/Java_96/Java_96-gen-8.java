        List<Integer> result = new ArrayList<>();
        if (n <= 1) return result;
        result.add(2);
        for (int i = 3; i < n; i += 2) {
            boolean is_prime = true;
            for (int j = 3; j < i; j += 2) {
                if (i % j == 0) {
                    is_prime = false;
                    break;
                }
            }
            if (is_prime) result.add(i);
        }
        return result;
    }
}

