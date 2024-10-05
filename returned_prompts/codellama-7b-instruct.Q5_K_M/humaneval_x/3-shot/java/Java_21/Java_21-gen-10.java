        double min_value = Collections.min(numbers);
        double max_value = Collections.max(numbers);

        List<Double> result = new ArrayList<>();

        for (double number : numbers) {
            result.add((number - min_value) / (max_value - min_value));
        }
        return result;
    }
}

