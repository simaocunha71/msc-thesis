        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                result.add((int) factorial(i));
            } else {
                result.add(sum(1, i));
            }
        }
        return result;
    }
}

