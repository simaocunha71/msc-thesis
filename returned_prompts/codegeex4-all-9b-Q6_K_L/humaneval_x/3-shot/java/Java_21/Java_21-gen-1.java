        double min = Collections.min(numbers);
        double max = Collections.max(numbers);

        List<Double> result = new ArrayList<>();
        for (double num : numbers) {
            result.add((num - min) / (max - min));
        }
        return result;

    }
}

