        if (lst.size() < 2) {
            return Optional.empty();
        }
        Collections.sort(lst);
        int smallest = lst.get(0);
        if (lst.get(1) == smallest) {
            return Optional.empty();
        }
        return Optional.of(lst.get(1));
    }
}

