        double mean = numbers.stream().mapToDouble(d -> d).average().orElse(0.0);
        double sum = 0.0;
        for (double num : numbers) {
            sum += Math.abs(num - mean);
        }
        return sum / numbers.size();
    }
}

