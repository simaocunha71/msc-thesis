        double min_diff = Double.MAX_VALUE;
        List<Double> result = new ArrayList<>();

        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double diff = Math.abs(numbers.get(i) - numbers.get(j));
                if (diff < min_diff) {
                    min_diff = diff;
                    result.clear();
                    result.add(numbers.get(i));
                    result.add(numbers.get(j));
                }
            }
        }
        return result;
    }
}

