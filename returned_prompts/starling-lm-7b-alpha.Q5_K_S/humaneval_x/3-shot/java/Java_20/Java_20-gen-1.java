        double min_difference = Double.MAX_VALUE;
        List<Double> result = null;
        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                if (Math.abs(numbers.get(i) - numbers.get(j)) < min_difference) {
                    min_difference = Math.abs(numbers.get(i) - numbers.get(j));
                    result = Arrays.asList(numbers.get(i), numbers.get(j));
                }
            }
        }
        return result;
    }
}

