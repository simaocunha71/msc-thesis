        Optional<Integer> maxNeg = Optional.empty();
        Optional<Integer> minPos = Optional.empty();

        for (int i : lst) {
            if (i < 0) {
                if (maxNeg.isPresent()) {
                    maxNeg = Optional.of(Math.max(maxNeg.get(), i));
                } else {
                    maxNeg = Optional.of(i);
                }
            } else if (i > 0) {
                if (minPos.isPresent()) {
                    minPos = Optional.of(Math.min(minPos.get(), i));
                } else {
                    minPos = Optional.of(i);
                }
            }
        }
        return List.of(maxNeg, minPos);
    }
}

