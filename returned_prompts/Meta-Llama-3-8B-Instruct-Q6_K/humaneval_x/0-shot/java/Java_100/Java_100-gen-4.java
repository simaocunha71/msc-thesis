    List<Integer> result = new ArrayList<Integer>();

    if (n <= 0) {
        return result;
    }

    result.add(n);
    int i = 1;
    while (n > 1) {
        if (i % 2 == 0) {
            n--;
        } else {
            n = n - (n - 1) / 2;
        }
        result.add(n);
        i++;
    }
    return result;
}
