        List<Integer> result = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            if (n % i == 0) {
                int count = 0;
                while (n % i == 0) {
                    n /= i;
                    count++;
                }
                result.add(i);
                if (count > 1) {
                    result.add(count);
                }
            }
        }
        return result;
    }
}

