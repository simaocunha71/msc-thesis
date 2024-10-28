        List<Integer> result = new ArrayList<>();
        result.add(1);
        result.add(3);

        if (n >= 2) {
            result.add(2);
        }

        for (int i = 3; i <= n; i++) {
            int sum = 0;
            if (i % 2 == 0) {
                sum = 1 + i / 2;
            } else {
                sum = result.get(i - 1) + result.get(i - 2) + result.get(i - 3);
            }
            result.add(sum);
        }
        return result;
    }
}

