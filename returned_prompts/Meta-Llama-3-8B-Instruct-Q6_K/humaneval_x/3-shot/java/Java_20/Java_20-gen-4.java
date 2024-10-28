        double min_diff = Double.MAX_VALUE;
        Double closest1 = null;
        Double closest2 = null;

        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double diff = Math.abs(numbers.get(i) - numbers.get(j));
                if (diff < min_diff) {
                    min_diff = diff;
                    closest1 = numbers.get(i);
                    closest2 = numbers.get(j);
                }
            }
        }
        List<Double> result = new ArrayList<>();
        result.add(closest1);
        result.add(closest2);
        return result;
    }
}

