    List<Integer> result = new ArrayList<Integer>();

    if (n == 0) {
        result.add(1);
        return result;
    }

    result.add(1);
    result.add(3);

    if (n == 1) {
        return result;
    }

    result.add(2);

    if (n == 2) {
        return result;
    }

    for (int i = 3; i <= n; i++) {
        if (i % 2 == 0) {
            result.add((int) Math.round((double) 1 + i / 2));
        } else {
            result.add(result.get(i - 1) + result.get(i - 2) + result.get(i - 3));
        }
    }

    return result;
}
