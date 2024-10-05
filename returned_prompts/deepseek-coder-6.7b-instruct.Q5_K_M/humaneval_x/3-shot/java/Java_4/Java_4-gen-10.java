        double mean 
        = numbers.stream().reduce(0.0, Double::sum) / numbers.size();
        return numbers.stream().mapToDouble(n -> Math.abs(n - mean)).sum() / numbers.size();
     }
}

