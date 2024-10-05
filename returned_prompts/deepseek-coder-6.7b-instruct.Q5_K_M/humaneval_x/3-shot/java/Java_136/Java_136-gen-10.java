        Optional<Integer> largest = lst.stream()
            .filter(n -> n < 0)
            .max(Integer::compareTo);

        Optional<Integer> smallest = lst.stream()
            .filter(n -> n > 0)
            .min(Integer::compareTo);

        return Arrays.asList(largest, smallest);
     }
}

