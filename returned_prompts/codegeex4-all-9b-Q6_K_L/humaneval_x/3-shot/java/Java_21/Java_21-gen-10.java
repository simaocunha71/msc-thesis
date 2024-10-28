        double min = Collections.min(numbers);
        double max = Collections.max(numbers);
        List<Double> result = new ArrayList<>();
        for (double n : numbers) {
            result.add((n - min) / (max - min));
        }
        return result;
    }
}

