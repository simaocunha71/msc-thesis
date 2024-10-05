        double min = Collections.min(numbers);
        double max = Collections.max(numbers);
        double range = max - min;

        List<Double> result = new ArrayList<>();
        for (double num : numbers) {
            double delta = num - min;
            double new_val = delta / range;
            result.add(new_val);
        }
        return result;
    }
}

