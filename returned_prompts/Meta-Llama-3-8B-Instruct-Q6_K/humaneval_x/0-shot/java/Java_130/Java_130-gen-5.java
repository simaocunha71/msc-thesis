    List<Integer> list = new ArrayList<>();
    if (n == 0) {
        list.add(1);
        return list;
    }
    list.add(1);
    list.add(3);
    for (int i = 2; i < n; i++) {
        if (i % 2 == 0) {
            list.add((int) Math.ceil((double) 1 / 2));
        } else {
            int a = list.get(i - 1);
            int b = list.get(i - 2);
            int c = list.get(i - 3);
            list.add(a + b + c);
        }
    }
    return list;
} // Time Complexity: O(n) where n is the given number. Space Complexity: O(n) for the list of Tribonacci sequence.