        double smallest_distance = Double.MAX_VALUE;
        double a = 0.0;
        double b = 0.0;

        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < smallest_distance) {
                    smallest_distance = distance;
                    a = numbers.get(i);
                    b = numbers.get(j);
                }
            }
        }
        List<Double> result = new ArrayList<>();
        result.add(a);
        result.add(b);
        return result;

    }
}

