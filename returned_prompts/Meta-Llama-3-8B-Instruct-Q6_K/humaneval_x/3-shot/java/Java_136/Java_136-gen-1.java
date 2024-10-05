        List<Optional<Integer>> result = new ArrayList<>();
        Optional<Integer> maxNeg = Optional.empty();
        Optional<Integer> minPos = Optional.empty();

        for (int num : lst) {
            if (num < 0) {
                if (maxNeg.isEmpty() || num > maxNeg.get()) {
                    maxNeg = Optional.of(num);
                }
            } else if (num > 0) {
                if (minPos.isEmpty() || num < minPos.get()) {
                    minPos = Optional.of(num);
                }
            }
        }
        result.add(maxNeg);
        result.add(minPos);
        return result;
    }
}

