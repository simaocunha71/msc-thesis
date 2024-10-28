        Collections.sort(numbers);
        double closest = Double.MAX_VALUE;
        List<Double> result = null;

        for (int i = 0; i < numbers.size() - 1; i++) {
            double distance = Math.abs(numbers.get(i) - numbers.get(i + 1));
            if (distance < closest) {
                closest = distance;
                result = Arrays.asList(numbers.get(i), numbers.get(i + 1));
            }
        }
        return result;
    }
}






```