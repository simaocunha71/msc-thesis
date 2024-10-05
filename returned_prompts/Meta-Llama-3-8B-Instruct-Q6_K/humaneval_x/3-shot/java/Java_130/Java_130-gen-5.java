        List<Integer> result = new ArrayList<>();
        if (n <= 0) return result;

        result.add(3);
        if (n == 1) return result;

        result.add(1);
        if (n == 2) return result;

        result.add(3);
        for (int i = 3; i <= n; i++) {
            int sum = 0;
            for (int j = 1; j <= i; j++) {
                if (j % 2 == 0) sum += j / 2;
                else sum += result.get(j - 1) + result.get(j - 2) + result.get(j - 3);
            }
            result.add(sum);
        }
        return result;
    }
}

