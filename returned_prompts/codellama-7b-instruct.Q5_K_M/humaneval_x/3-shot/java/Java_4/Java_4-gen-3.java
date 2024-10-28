        double mean = numbers.stream().mapToDouble(Double::doubleValue).average().getAsDouble();
        return numbers.stream().mapToDouble(number -> Math.abs(number - mean)).average().getAsDouble();
    }
}

