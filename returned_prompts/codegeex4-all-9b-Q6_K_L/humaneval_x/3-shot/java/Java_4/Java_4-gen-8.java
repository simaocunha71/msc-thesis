        double mean = numbers.stream().mapToDouble(Double::doubleValue).average().getAsDouble();
        double mad = numbers.stream().mapToDouble(x -> Math.abs(x - mean)).average().getAsDouble();
        return mad;
    }
}

