        Optional<Integer> largestNegative = lst.stream().filter(x -> x < 0).max(Comparator.naturalOrder());
        Optional<Integer> smallestPositive = lst.stream().filter(x -> x > 0).min(Comparator.naturalOrder());
        return Arrays.asList(largestNegative, smallestPositive);
    }
}

