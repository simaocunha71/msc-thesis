        List<Optional<Integer>> result = new ArrayList<>();
        result.add(findLargestNegative(lst));
        result.add(findSmallestPositive(lst));
        return result;
    }

    public Optional<Integer> findLargestNegative(List<Integer> lst) {
        Optional<Integer> largest = Optional.empty();

        for (Integer i : lst) {
            if (i < 0) {
                if (!largest.isPresent() || i > largest.get()) {
                    largest = Optional.of(i);
                }
            }
        }
        return largest;
    }

    public Optional<Integer> findSmallestPositive(List<Integer> lst) {
        Optional<Integer> smallest = Optional.empty();

        for (Integer i : lst) {
            if (i > 0) {
                if (!smallest.isPresent() || i < smallest.get()) {
                    smallest = Optional.of(i);
                }
            }
        }
        return smallest;
    }
}

