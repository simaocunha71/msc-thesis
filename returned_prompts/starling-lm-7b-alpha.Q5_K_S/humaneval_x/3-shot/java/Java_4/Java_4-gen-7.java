        double mean = numbers.stream().mapToDouble(a -> a).average().getAsDouble();
        return numbers.stream().mapToDouble(a -> Math.abs(a - mean)).average().getAsDouble();
    }
}

