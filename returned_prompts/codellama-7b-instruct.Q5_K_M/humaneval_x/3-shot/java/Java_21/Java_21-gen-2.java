        double min = Collections.min(numbers);
        double max = Collections.max(numbers);
        double range = max - min;

        List<Double> result = new ArrayList<>();
        for (double x : numbers) {
            result.add((x - min) / range);
        }
        return result;
    }
}

