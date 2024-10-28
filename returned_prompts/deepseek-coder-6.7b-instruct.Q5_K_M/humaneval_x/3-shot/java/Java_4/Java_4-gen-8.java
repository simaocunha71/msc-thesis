        double mean = numbers.stream().reduce(0.0, Double::sum) / numbers.size();
        return numbers.stream().mapToDouble(x -> Math.abs(x - mean)).sum() / numbers.size();
     }
}

