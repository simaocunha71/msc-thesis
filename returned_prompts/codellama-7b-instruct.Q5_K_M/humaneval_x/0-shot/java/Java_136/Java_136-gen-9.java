        List<Optional<Integer>> result = new ArrayList<>();

        Optional<Integer> largestNegative = null;
        Optional<Integer> smallestPositive = null;

        for (Integer i : lst){
            if (i < 0 && (largestNegative == null || i > largestNegative)){
                largestNegative = i;
            }
            if (i > 0 && (smallestPositive == null || i < smallestPositive)){
                smallestPositive = i;
            }
        }

        result.add(largestNegative);
        result.add(smallestPositive);

        return result;
    }
}
