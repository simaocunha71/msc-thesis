    for (int i = 0; i < l.size(); i++) {
        l.set(i, l.get(i) + 1);
    }
    Collections.sort(l);
    Collections.reverse(l);
    return l