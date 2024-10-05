    List<Integer> res = new ArrayList<>();
    for (int i = n; i != 1; i = next(i)) {
        if (isOdd(i)) {
            res.add(i);
        }
    }
    res.add(1);
    Collections.sort(res);
    return res;
}

private boolean isOdd(int n) {
    return n % 2 != 0;
}

private int next(int n) {
    return isEven(n) ? n / 2 : n * 3 + 1;
}

private boolean isEven(int n) {
    return n % 2 == 0;
}
