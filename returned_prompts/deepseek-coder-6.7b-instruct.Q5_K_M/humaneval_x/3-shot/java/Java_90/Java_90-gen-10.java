        if (lst.size() < 2) return Optional.empty();
        int firstMin = Integer.MAX_VALUE;
        int secondMin = Integer.MAX_VALUE;

        for (int n : lst) {
            if (n < firstMin) {
                secondMin = firstMin;
                firstMin = n;
            } else if (n > firstMin && n < secondMin) {
                secondMin = n;
            }
        }

        return secondMin == Integer.MAX_VALUE ? Optional.empty() : Optional.of(secondMin);
    }
}

