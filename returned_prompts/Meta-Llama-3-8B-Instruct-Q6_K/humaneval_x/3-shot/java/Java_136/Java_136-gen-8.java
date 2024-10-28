        Optional<Integer> maxNeg = Optional.empty();
        Optional<Integer> minPos = Optional.empty();

        for (int i : lst) {
            if (i < 0) {
                maxNeg = Optional.of(i);
            } else if (i > 0) {
                minPos = Optional.of(i);
            }
        }

        return new ArrayList<>(Arrays.asList(maxNeg, minPos));
    }
}