        if (lst.size() < 2) return Optional.empty();

        Integer min = lst.get(0);
        Integer secondMin = null;

        for (int num : lst) {
            if (num < min) {
                secondMin = min;
                min = num;
            } else if (num < secondMin) {
                secondMin = num;
            }
        }
        return secondMin != null ? Optional.of(secondMin) : Optional.empty();
    }
}