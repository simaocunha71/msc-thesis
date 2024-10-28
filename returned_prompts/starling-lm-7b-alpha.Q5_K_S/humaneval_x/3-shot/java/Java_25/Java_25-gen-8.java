        List<Integer> result = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            if (n % i == 0) {
                result.add(i);
                while (n % i == 0) {
                    n /= i;
                }
            }
        }
        return result;
    }
}

