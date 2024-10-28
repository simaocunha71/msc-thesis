    List<Integer> pile = new ArrayList<>();
    if (n <= 0) {
        return pile;
    }
    pile.add(n);
    int level = 1;
    while (n > 0) {
        if (n % 2 == 1) {
            pile.add(level * 2 + 1);
            n -= level * 2 + 1;
        } else {
            pile.add(level * 2);
            n -= level * 2;
        }
        level++;
    }
    return pile;
}
