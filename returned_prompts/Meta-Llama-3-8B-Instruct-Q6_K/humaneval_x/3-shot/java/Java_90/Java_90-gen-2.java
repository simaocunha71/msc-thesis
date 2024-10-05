        if (lst.size() < 2) {
            return Optional.empty();
        }

        Integer min = lst.get(0);
        Integer secondMin = null;

        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < min) {
                secondMin = min;
                min = lst.get(i);
            } else if (lst.get(i) < secondMin) {
                secondMin = lst.get(i);
            }
        }

        return secondMin != null ? Optional.of(secondMin) : Optional.empty();
    }
}

