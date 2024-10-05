        Collections.sort(numbers);
        List<Double> result = Arrays.asList(numbers.get(0), numbers.get(1));
        double distance = Math.abs(result.get(0) - result.get(1));
        for (int i = 1; i < numbers.size(); i++) {
            double distance_i = Math.abs(result.get(0) - numbers.get(i));
            if (distance_i < distance) {
                result.set(0, numbers.get(i));
                result.set(1, result.get(0) + 1);
                distance = distance_i;
            } else {
                double distance_i_1 = Math.abs(result.get(1) - numbers.get(i));
                if (distance_i_1 < distance) {
                    result.set(1, numbers.get(i));
                    distance = distance_i_1;
                }
            }
        }
        return result;
    }
}

