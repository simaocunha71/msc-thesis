        if (lst.size() < 2) return Optional.empty();
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) < min) {
                min = lst.get(i);
            }
        }
        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) == min) {
                if (i + 1 < lst.size()) {
                    return Optional.of(lst.get(i + 1));
                } else {
                    return Optional.empty();
                }
            }
        }
        return Optional.empty();
    }
}

