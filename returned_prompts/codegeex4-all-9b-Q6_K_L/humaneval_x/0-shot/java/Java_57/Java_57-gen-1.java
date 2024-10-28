public boolean monotonic(List<Integer> l) {
    if (l.size() < 2) {
        return true;
    }

    int direction = Integer.compare(l.get(1), l.get(0));

    for (int i = 2; i < l.size(); i++) {
        int currentDirection = Integer.compare(l.get(i), l.get(i - 1));

        if (currentDirection != 0 && currentDirection != direction) {
            return false;
        }
    }

    return true;
}