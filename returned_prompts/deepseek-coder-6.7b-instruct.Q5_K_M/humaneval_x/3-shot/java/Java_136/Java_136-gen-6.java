        List<Integer> negatives = new ArrayList<>();
        List<Integer> positives = new ArrayList<>();

        for(int num : lst) {
            if(num < 0) negatives.add(num);
            if(num > 0) positives.add(num);
        }

        Optional<Integer> largestNegative = negatives.isEmpty() ? Optional.empty() : Optional.of(Collections.max(negatives));
        Optional<Integer> smallestPositive = positives.isEmpty() ? Optional.empty() : Optional.of(Collections.min(positives));

        return Arrays.asList(largestNegative, smallestPositive);
     }
}

