        if (lst.size() <= 1)
            return Optional.empty();

        int smallest = lst.get(0);
        int second_smallest = -1;

        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < smallest) {
                second_smallest = smallest;
                smallest = lst.get(i);
            } else if (lst.get(i) < second_smallest || second_smallest == -1) {
                second_smallest = lst.get(i);
            }
        }

        if (second_smallest == -1)
            return Optional.empty();
        else
            return Optional.of(second_smallest);
    }
}

