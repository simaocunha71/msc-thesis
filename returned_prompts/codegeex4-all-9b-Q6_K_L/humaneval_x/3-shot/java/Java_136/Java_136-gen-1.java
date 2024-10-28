        Optional<Integer> largest_negative = lst.stream()
                .filter(x -> x < 0)
                .max(Integer::compareTo);

        Optional<Integer> smallest_positive = lst.stream()
                .filter(x -> x > 0)
                .min(Integer::compareTo);

        return Arrays.asList(largest_negative, smallest_positive);

    }
}

