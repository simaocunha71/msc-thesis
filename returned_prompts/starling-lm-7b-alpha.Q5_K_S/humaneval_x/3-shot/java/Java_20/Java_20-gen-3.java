        Collections.sort(numbers);
        List<Double> result = new ArrayList<>();
        result.add(numbers.get(0));
        result.add(numbers.get(1));
        double min_distance = result.get(1) - result.get(0);
        for (int i = 1; i < numbers.size(); i++) {
            double distance = result.get(1) - numbers.get(i);
            if (distance < min_distance) {
                min_distance = distance;
                result.set(0, result.get(1));
                result.set(1, numbers.get(i));
            }
        }
        return result;
    }
}

