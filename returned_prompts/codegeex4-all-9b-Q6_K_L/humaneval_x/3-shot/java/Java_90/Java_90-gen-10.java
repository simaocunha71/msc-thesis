        if (lst.size() < 2) {
            return Optional.empty();
        }

        int smallest = Integer.MAX_VALUE;
        int second_smallest = Integer.MAX_VALUE;

        for (int num : lst) {
            if (num < smallest) {
                second_smallest = smallest;
                smallest = num;
            } else if (num < second_smallest && num > smallest) {
                second_smallest = num;
            }
        }

        if (second_smallest == Integer.MAX_VALUE) {
            return Optional.empty();
        } else {
            return Optional.of(second_smallest);
        }
    }
}

