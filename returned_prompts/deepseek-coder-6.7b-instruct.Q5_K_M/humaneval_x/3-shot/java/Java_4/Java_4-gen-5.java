        double mean = numbers.stream().mapToDouble(val -> val).average().orElse(0.0);
        return numbers.stream().mapToDouble(val -> Math.abs(val - mean)).average().orElse(0.0);
     }
}

