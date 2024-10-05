        double min_number = Collections.min(numbers);
        double max_number = Collections.max(numbers);
        double range = max_number - min_number;
        List<Double> result = new ArrayList<>();
        for (double number : numbers) {
            result.add((number - min_number) / range);
        }
        return result;
    }
}

