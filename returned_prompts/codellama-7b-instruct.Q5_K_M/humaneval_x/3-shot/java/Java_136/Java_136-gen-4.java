        Optional<Integer> largestNeg = Optional.empty();
        Optional<Integer> smallestPos = Optional.empty();

        for (Integer x : lst) {
            if (x < 0 && (largestNeg.isEmpty() || x > largestNeg.get())) {
                largestNeg = Optional.of(x);
            }
            if (x > 0 && (smallestPos.isEmpty() || x < smallestPos.get())) {
                smallestPos = Optional.of(x);
            }
        }

        return Arrays.asList(largestNeg, smallestPos);
    }
}

