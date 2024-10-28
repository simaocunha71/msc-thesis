        double mean = numbers.stream().mapToDouble(Double::doubleValue).average().getAsDouble();
        return numbers.stream().mapToDouble(x -> Math.abs(x - mean)).average().getAsDouble();
    }
}

