        double min = Collections.min(numbers);
        double max = Collections.max(numbers);
        List<Double> result = new ArrayList<>();
        for (double d : numbers) {
            result.add((d - min) / (max - min));
        }
        return result;
    }
}

