        if (lst.size() < 2) return Optional.empty();
        int min = Integer.MAX_VALUE;
        int second_min = Integer.MAX_VALUE;

        for (int num : lst) {
            if (num < min) {
                second_min = min;
                min = num;
            } else if (num > min && num < second_min) {
                second_min = num;
            }
        }

        return (second_min == Integer.MAX_VALUE) ? Optional.empty() : Optional.of(second_min);
    }
}

