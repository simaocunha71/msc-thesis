        double min_distance = Double.MAX_VALUE;
        Double closest_pair = null;

        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < min_distance) {
                    min_distance = distance;
                    closest_pair = new ArrayList<>();
                    closest_pair.add(numbers.get(i));
                    closest_pair.add(numbers.get(j));
                }
            }
        }
        return closest_pair;
    }
}

