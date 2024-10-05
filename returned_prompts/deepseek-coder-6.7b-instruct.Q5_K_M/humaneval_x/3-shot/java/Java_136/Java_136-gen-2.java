        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();

        for(Integer i : lst){
            if(i < 0 && (largestNegative.isEmpty() || i > largestNegative.get())){
                largestNegative = Optional.of(i);
            } else if(i > 0 && (smallestPositive.isEmpty() || i < smallestPositive.get())){
                smallestPositive = Optional.of(i);
            }
        }

        return Arrays.asList(largestNegative, smallestPositive);
    }
}

