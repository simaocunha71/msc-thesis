        double mean = numbers.stream().mapToDouble(Double::doubleValue).average().getAsDouble();
        double sum = numbers.stream().map(v -> Math.abs(v - mean)).mapToDouble(Double::doubleValue).sum();
        return sum / numbers.size();
    }
}

