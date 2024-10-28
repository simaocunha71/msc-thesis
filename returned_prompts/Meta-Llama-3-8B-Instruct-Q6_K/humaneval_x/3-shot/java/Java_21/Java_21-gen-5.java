        double min = Collections.min(numbers);
        double max = Collections.max(numbers);

        List<Double> rescaled = new ArrayList<>();
        for (double num : numbers) {
            rescaled.add((num - min) / (max - min));
        }
        return rescaled;
    }
}

