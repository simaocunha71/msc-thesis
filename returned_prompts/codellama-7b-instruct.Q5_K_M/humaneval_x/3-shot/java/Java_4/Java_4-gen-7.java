        double mean = numbers.stream().mapToDouble(n -> n).average().getAsDouble();
        double deviation = numbers.stream().map(n -> Math.abs(n - mean)).mapToDouble(n -> n).average().getAsDouble();
        return deviation;
    }
}

