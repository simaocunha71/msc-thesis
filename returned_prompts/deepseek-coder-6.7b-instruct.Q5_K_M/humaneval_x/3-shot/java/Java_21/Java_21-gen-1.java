        double min = Collections.min(numbers);
        double max = Collections.max(numbers);
        double range = max - min;

        List<Double> result = new ArrayList<>();
        for(double num: numbers) {
            result.add((num - min) / range);
        }
        return result;
     }
}

