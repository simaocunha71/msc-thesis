        List<Double> result = new ArrayList<>();
        double min = Collections.min(numbers);
        double max = Collections.max(numbers);
        double range = max - min;
        for (Double number : numbers) {
            result.add((number - min) / range);
        }
        return result;
    }
}

