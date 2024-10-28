public double meanAbsoluteDeviation(List<Double> numbers) {
        // Find the mean of the numbers
        double mean = numbers.stream().mapToDouble(Double::doubleValue).average().orElse(0.0);
        
        // Calculate the absolute difference between each number and the mean
        List<Double> differences = numbers.stream()
                .map(num -> Math.abs(num - mean))
                .collect(Collectors.toList());
        
        // Calculate the average of the differences
        double averageDifference = differences.stream().mapToDouble(Double::doubleValue).average().orElse(0.0);
        
        return averageDifference;
    }