        if (lst.size() < 2) return Optional.empty();

        int min = Integer.MAX_VALUE;
        int secondMin = Integer.MAX_VALUE;

        for (int num : lst) {
            if (num < min) {
                secondMin = min;
                min = num;
            } else if (num > min && num < secondMin) {
                secondMin = num;
            }
        }

        return (secondMin == Integer.MAX_VALUE) ? Optional.empty() : Optional.of(secondMin);
    }
}

