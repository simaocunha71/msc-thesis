        if (lst.size() == 1) {
            return Optional.empty();
        }
        Optional<Integer> result = Optional.empty();
        int smallest = lst.get(0);
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < smallest) {
                result = Optional.of(lst.get(i));
                smallest = lst.get(i);
            }
        }
        return result;
    }
}

