        List<Integer> result = new ArrayList<>();
        if (n <= 1) return result;

        for (int i = 2; i < n; i++) {
            boolean is_prime = true;
            for (int j = 2; j <= Math.sqrt(i); j++) {
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

