        int smallest = lst.get(0);
        int second_smallest = -1;

        for (int num : lst) {
            if (num < smallest) {
                second_smallest = smallest;
                smallest = num;
            } else if (second_smallest == -1 && num > smallest) {
                second_smallest = num;
            }
        }
        if (second_smallest == -1) return Optional.empty();
        else return Optional.of(second_smallest);
    }
}

