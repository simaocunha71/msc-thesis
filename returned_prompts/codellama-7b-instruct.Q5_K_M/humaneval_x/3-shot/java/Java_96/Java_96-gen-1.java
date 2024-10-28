        List<Integer> result = new ArrayList<>();
        for (int i = 2; i < n; i++) {
            boolean is_prime = true;
            for (int j = 2; j < i; j++) {
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

