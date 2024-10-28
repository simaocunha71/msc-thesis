        Integer secondSmallest = null;
        Integer smallest = null;
        for (Integer i : lst) {
            if (smallest == null || i < smallest) {
                smallest = i;
            } else {
                if (secondSmallest == null || i < secondSmallest) {
                    secondSmallest = i;
                }
            }
        }
        return Optional.ofNullable(secondSmallest);
    }
}
