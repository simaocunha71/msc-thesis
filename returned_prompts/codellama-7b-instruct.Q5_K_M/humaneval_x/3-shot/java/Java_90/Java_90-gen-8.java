        if (lst.size() < 2) return Optional.empty();
        int min = Integer.MAX_VALUE;
        int min_index = -1;
        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) < min) {
                min = lst.get(i);
                min_index = i;
            }
        }
        if (lst.get(min_index) == lst.get(1)) return Optional.empty();
        else return Optional.of(lst.get(min_index));
    }
}

