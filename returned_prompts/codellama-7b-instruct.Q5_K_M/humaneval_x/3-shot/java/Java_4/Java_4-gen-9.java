        double mean = numbers.stream().mapToDouble(Double::doubleValue).sum() / numbers.size();
        double sum = numbers.stream().mapToDouble(x -> Math.abs(x - mean)).sum();
        return sum / numbers.size();
    }
}

