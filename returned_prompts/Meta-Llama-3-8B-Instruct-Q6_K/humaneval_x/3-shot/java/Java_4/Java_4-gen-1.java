        double mean = 0.0;
        double sum = 0.0;
        for (double num : numbers) {
            sum += num;
        }
        mean = sum / numbers.size();
        sum = 0.0;
        for (double num : numbers) {
            sum += Math.abs(num - mean);
        }
        return sum / numbers.size();
    }
}

