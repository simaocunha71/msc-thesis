        if (lst.size() <= 1) {
            return Optional.empty();
        }
        int min_value = lst.get(0);
        int min_index = 0;
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < min_value) {
                min_value = lst.get(i);
                min_index = i;
            }
        }
        if (min_index == lst.size() - 1) {
            return Optional.of(lst.get(0));
        } else {
            return Optional.of(lst.get(min_index + 1));
        }
    }
}

