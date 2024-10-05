        if (lst.size() < 2) {
            return Optional.empty();
        }
        int first = lst.get(0);
        int second = lst.get(1);
        int current_smallest = second;
        for (int i = 2; i < lst.size(); i++) {
            if (lst.get(i) < first) {
                current_smallest = first;
                first = lst.get(i);
            } else if (lst.get(i) < current_smallest) {
                current_smallest = lst.get(i);
            }
        }
        return Optional.of(current_smallest);
    }
}

