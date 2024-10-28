        List<Double> result = Arrays.asList(Double.MAX_VALUE, Double.MIN_VALUE);

        for (double number : numbers) {
            if (number < result.get(0)) {
                result.set(0, number);
            } else if (number > result.get(1)) {
                result.set(1, number);
            }
        }
        return result;
    }
}

