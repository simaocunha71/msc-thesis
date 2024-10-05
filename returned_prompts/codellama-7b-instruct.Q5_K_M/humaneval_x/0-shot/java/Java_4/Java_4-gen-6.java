        // TODO: Calculate the mean of the input list
        double mean = numbers.stream().mapToDouble(Double::doubleValue).average().orElse(0.0);

        // TODO: Calculate the MAD by iterating over the list
        // Hint: use Math.abs() to calculate the absolute difference
        // Hint 2: You need to sum the absolute differences
        // Hint 3: Average the sum of absolute differences to get the MAD
        double mad = 0.0;
        for (double number : numbers) {
            mad += Math.abs(number - mean);
        }
        mad /= numbers.size();

        return mad;
    }
}
