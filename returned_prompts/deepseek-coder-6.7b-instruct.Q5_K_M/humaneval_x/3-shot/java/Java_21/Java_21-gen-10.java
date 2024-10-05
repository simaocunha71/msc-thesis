        double min = Collections.min(numbers);
        double max = Collections.max(numbers);
        List<Double> result = new ArrayList<>();

        for (double number : numbers) {
            result.add((number - min) / (max - min));
        }

        return result;
     }
}

