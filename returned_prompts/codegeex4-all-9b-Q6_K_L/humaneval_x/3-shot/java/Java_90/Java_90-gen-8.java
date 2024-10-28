        if (lst.size() < 2) return Optional.empty();

        int smallest = Integer.MAX_VALUE;
        int second_smallest = Integer.MAX_VALUE;

        for (int i : lst) {
            if (i < smallest) {
                second_smallest = smallest;
                smallest = i;
            } else if (i < second_smallest) {
                second_smallest = i;
            }
        }

        return second_smallest != Integer.MAX_VALUE ? Optional.of(second_smallest) : Optional.empty();
    }
}

