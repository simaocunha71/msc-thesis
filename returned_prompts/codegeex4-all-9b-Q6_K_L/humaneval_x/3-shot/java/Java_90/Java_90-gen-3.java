        if (lst.size() < 2) return Optional.empty();

        int smallest = lst.get(0);
        int second_smallest = lst.get(1);

        if (smallest > second_smallest) {
            int temp = smallest;
            smallest = second_smallest;
            second_smallest = temp;
        }

        for (int i = 2; i < lst.size(); i++) {
            int current = lst.get(i);
            if (current < smallest) {
                second_smallest = smallest;
                smallest = current;
            } else if (current < second_smallest) {
                second_smallest = current;
            }
        }

        return (second_smallest == smallest) ? Optional.empty() : Optional.of(second_smallest);
    }
}

