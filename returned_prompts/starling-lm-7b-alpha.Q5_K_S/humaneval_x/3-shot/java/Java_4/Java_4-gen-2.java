        double mean = numbers.stream().mapToDouble(d -> d).average().getAsDouble();
        return numbers.stream().mapToDouble(d -> Math.abs(d - mean)).average().getAsDouble();
    }
}

