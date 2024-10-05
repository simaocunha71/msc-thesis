        double mean = numbers.stream().mapToDouble(i -> i).average().getAsDouble();
        return numbers.stream().mapToDouble(i -> Math.abs(i - mean)).average().getAsDouble();
    }
}


