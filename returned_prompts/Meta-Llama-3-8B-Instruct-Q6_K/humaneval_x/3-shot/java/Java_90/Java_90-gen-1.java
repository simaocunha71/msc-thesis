        Optional<Integer> smallest = Optional.empty();
        Optional<Integer> nextSmallest = Optional.empty();

        for (int num : lst) {
            if (!smallest.isPresent() || num < smallest.get()) {
                nextSmallest = smallest;
                smallest = Optional.of(num);
            } else if (!nextSmallest.isPresent() && num > smallest.get() && num < nextSmallest.get()) {
                nextSmallest = Optional.of(num);
            }
        }

        return nextSmallest.isPresent() ? nextSmallest : Optional.empty();
    }
}