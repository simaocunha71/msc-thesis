        if (lst.size() < 2) {
            return Optional.empty();
        }

        int smallest = lst.get(0);
        int second_smallest = Integer.MAX_VALUE;

        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < smallest) {
                second_smallest = smallest;
                smallest = lst.get(i);
            } else if (lst.get(i) < second_smallest && lst.get(i) != smallest) {
                second_smallest = lst.get(i);
            }
        }
        return Optional.of(second_smallest);
    }
}

