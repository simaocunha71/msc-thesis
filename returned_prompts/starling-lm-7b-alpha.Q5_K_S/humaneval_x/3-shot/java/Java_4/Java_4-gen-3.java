        double mean = numbers.stream().mapToDouble(Double::doubleValue).average().getAsDouble();
        double mad = numbers.stream().map(x -> Math.abs(x - mean)).mapToDouble(Double::doubleValue).average().getAsDouble();
        return mad;
    }
}

