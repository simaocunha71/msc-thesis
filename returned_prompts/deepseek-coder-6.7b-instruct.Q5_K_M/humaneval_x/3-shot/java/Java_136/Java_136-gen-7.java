        Optional<Integer> largestNegative = lst.stream()
            .filter(n -> n < 0)
            .max(Integer::compareTo);

        Optional<Integer> smallestPositive = lst.stream()
            .filter(n -> n > 0)
            .min(Integer::compareTo);

        return Arrays.asList(largestNegative, smallestPositive);
     }
}

