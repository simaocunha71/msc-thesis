        if (lst.isEmpty() || lst.size() <= 1) {
            return Optional.empty();
        }
        Collections.sort(lst);
        int smallest = lst.get(0);
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) > smallest) {
                return Optional.of(lst.get(i));
            }
        }
        return Optional.empty();
    }
} 