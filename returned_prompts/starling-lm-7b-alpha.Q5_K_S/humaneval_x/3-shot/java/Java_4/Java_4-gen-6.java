        double sum = 0;
        for (double number : numbers) {
            sum += Math.abs(number - mean(numbers));
        }
        return sum / numbers.size();
    }

    public double mean(List<Double> numbers) {
        double sum = 0;
        for (double number : numbers) {
            sum += number;
        }
        return sum / numbers.size();
    }
}

