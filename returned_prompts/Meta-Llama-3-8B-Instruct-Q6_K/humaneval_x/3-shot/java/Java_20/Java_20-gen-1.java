        double min_diff = Double.MAX_VALUE;
        List<Double> closest_elements = new ArrayList<>();

        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double diff = Math.abs(numbers.get(i) - numbers.get(j));
                if (diff < min_diff) {
                    min_diff = diff;
                    closest_elements.clear();
                    closest_elements.add(numbers.get(i));
                    closest_elements.add(numbers.get(j));
                } else if (diff == min_diff) {
                    closest_elements.add(numbers.get(i));
                    closest_elements.add(numbers.get(j));
                }
            }
        }
        Collections.sort(closest_elements);
        return closest_elements;
    }
}

