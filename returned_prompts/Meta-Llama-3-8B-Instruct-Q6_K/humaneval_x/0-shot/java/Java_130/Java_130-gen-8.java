    List<Integer> result = new ArrayList<>();
    result.add(3);
    if (n > 0) {
        result.add(1);
        if (n > 1) {
            result.add(3);
            for (int i = 3; i <= n; i++) {
                if (i % 2 == 0) {
                    result.add(1 + i / 2);
                } else {
                    int sum = 0;
                    for (int j = 1; j <= 3; j++) {
                        sum += result.get(result.size() - j);
                    }
                    result.add(sum);
                }
            }
        }
    }
    return result;
}

