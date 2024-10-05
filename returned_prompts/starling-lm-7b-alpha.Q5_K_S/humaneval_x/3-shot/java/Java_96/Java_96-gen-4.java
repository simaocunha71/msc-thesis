        List<Integer> result = new ArrayList<>();
        result.add(2);
        result.add(3);
        for (int i = 5; i < n; i += 2) {
            boolean is_prime = true;
            for (int j = 3; j * j <= i; j += 2) {
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

