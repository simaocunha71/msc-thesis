        List<Optional<Integer>> result = new ArrayList<>(Arrays.asList(Optional.empty(), Optional.empty()));
        int largestNegative = Integer.MIN_VALUE;
        int smallestPositive = Integer.MAX_VALUE;
        for (Integer num : lst) {
            if (num < 0 && num > largestNegative) {
                largestNegative = num;
            } else if (num > 0 && num < smallestPositive) {
                smallestPositive = num;
            }
        }

        if (largestNegative != Integer.MIN_VALUE) {
            result.set(0, Optional.of(largestNegative));
        }

        if (smallestPositive != Integer.MAX_VALUE) {
            result.set(1, Optional.of(smallestPositive));
        }

        return result;
     }
}

