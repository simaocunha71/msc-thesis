        Optional<Integer> maxNegative = Optional.empty();
        Optional<Integer> minPositive = Optional.empty();

        for (int i = 0; i < lst.size(); i++){
            if (lst.get(i) < 0){
                if (maxNegative.isPresent() && lst.get(i) < maxNegative.get()){
                    continue A;
                }
                maxNegative = Optional.of(lst.get(i));
            } else {
                if (minPositive.isPresent() && lst.get(i) < minPositive.get()){
                    continue A;
                }
                minPositive = Optional.of(lst.get(i));
            }
        }

        return Arrays.asList(maxNegative, minPositive);
    }
}
