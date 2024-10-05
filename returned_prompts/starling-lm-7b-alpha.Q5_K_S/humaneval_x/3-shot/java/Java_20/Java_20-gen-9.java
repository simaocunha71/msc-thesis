        Collections.sort(numbers);
        List<Double> result = new ArrayList<>();
        result.add(numbers.get(0));
        result.add(numbers.get(1));

        double min_distance = Math.abs(numbers.get(0) - numbers.get(1));

        for (int i = 1; i < numbers.size(); i++) {
            double distance = Math.abs(numbers.get(i) - numbers.get(i - 1));
            if (distance < min_distance) {
                min_distance = distance;
                result.set(0, numbers.get(i));
                result.set(1, numbers.get(i - 1));
            }
        }
        return result;
    }
}

