        double min_val = Collections.min(numbers);
        double max_val = Collections.max(numbers);
        double range = max_val - min_val;

        List<Double> result = new ArrayList<>();
        for (double n : numbers) {
            result.add((n - min_val) / range);
        }
        return result;
    }
}

