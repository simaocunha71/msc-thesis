        double min_distance = Double.MAX_VALUE;
        Double closest1 = null;
        Double closest2 = null;

        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < min_distance) {
                    min_distance = distance;
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

