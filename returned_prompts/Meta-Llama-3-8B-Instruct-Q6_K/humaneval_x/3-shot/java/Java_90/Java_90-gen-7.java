        if (lst.size() < 2) {
            return Optional.empty();
        }

        int min = lst.get(0);
        int secondMin = Integer.MAX_VALUE;

        for (int i : lst) {
            if (i < min) {
                secondMin = min;
                min = i;
            } else if (i < secondMin) {
                secondMin = i;
            }
        }

        return secondMin == Integer.MAX_VALUE ? Optional.empty() : Optional.of(secondMin);
    }
}

