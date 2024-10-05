        Optional<Integer> maxNeg = lst.stream()
            .filter(i -> i < 0)
            .max(Integer::compareTo);

        Optional<Integer> minPos = lst.stream()
            .filter(i -> i > 0)
            .min(Integer::compareTo);

        return Arrays.asList(maxNeg, minPos);
    }
}

