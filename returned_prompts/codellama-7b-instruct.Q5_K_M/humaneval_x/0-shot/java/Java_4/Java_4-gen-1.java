        double sum = 0.0;
        double mean = mean(numbers);
        for (Double x : numbers)
            sum += Math.abs(x - mean);
        return sum / numbers.size();
    }

    /**
    Calculate the average of the given list of numbers
    >>> mean(Arrays.asList(1.0, 2.0, 3.0, 4.0))
    2.5
     */
    public double mean(List<Double> numbers) {
        double sum = 0.0;
        for (Double x : numbers)
            sum += x;
        return sum / numbers.size();
    }
}

