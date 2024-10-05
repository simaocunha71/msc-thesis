        if (lst.size() < 2) return Optional.empty();
        int smallest = Integer.MAX_VALUE;
        int secondSmallest = Integer.MAX_VALUE;
        for (int num : lst) {
            if (num < smallest) {
                secondSmallest = smallest;
                smallest = num;
            } else if (num < secondSmallest && num != smallest) {
                secondSmallest = num;
            }
        }
        return (secondSmallest == Integer.MAX_VALUE) ? Optional.empty() : Optional.of(secondSmallest);
    }
}

