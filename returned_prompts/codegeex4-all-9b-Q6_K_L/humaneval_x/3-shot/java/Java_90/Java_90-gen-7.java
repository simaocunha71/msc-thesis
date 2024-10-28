        if (lst.size() < 2) {
            return Optional.empty();
        }

        int min = Integer.MAX_VALUE;
        int second_min = Integer.MAX_VALUE;

        for (int n : lst) {
            if (n < min) {
                second_min = min;
                min = n;
            } else if (n < second_min && n > min) {
                second_min = n;
            }
        }

        if (second_min == Integer.MAX_VALUE) {
            return Optional.empty();
        } else {
            return Optional.of(second_min);
        }

    }
}

