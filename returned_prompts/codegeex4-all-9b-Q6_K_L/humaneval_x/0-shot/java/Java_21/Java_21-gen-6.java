public List<Double> rescaleToUnit(List<Double> numbers) {
        Double max = Collections.max(numbers);
        Double min = Collections.min(numbers);
        return numbers.stream().map(n -> (n - min) / (max - min)).collect(Collectors.toList());
    }