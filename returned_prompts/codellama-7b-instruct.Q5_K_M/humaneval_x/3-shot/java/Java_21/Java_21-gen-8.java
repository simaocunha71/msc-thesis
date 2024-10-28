        double min = Collections.min(numbers);
        double max = Collections.max(numbers);
        double range = max - min;
        List<Double> result = new ArrayList<>();

        for (double number : numbers) {
            result.add((number - min) / range);
        }
        return result;
    }
}

