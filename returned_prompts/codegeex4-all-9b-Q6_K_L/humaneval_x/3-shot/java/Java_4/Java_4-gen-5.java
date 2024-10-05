        double mean = numbers.stream()
                .reduce(0.0, Double::sum) / numbers.size();

        return numbers.stream()
                .mapToDouble(number -> Math.abs(number - mean))
                .average()
                .getAsDouble();
    }
}

