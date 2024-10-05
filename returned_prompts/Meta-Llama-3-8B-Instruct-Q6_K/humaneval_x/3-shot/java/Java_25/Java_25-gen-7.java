        List<Integer> result = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            if (n % i == 0) {
                int count = 0;
                while (n % i == 0) {
                    n /= i;
                    count++;
                }
                result.add(i);
                for (int j = 0; j < count; j++) {
                    result.add(i);
                }
            }
        }
        return result;
    }
}

