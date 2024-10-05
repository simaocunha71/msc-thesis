    List<Integer> result = new ArrayList<>();
    HashSet<Integer> set = new HashSet<>();
    while (n != 1) {
        set.add(n);
        if (n % 2 == 0) {
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
    }
    set.add(1);
    for (int num : set) {
        if (num % 2 != 0) {
            result.add(num);
        }
    }
    Collections.sort(result);
    return result;
}
