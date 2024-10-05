        double sum = 0;
        for (double i : numbers) {
            sum += i;
        }
        double mean = sum / numbers.size();
        double sum1 = 0;
        for (double i : numbers) {
            sum1 += Math.abs(i - mean);
        }
        return sum1 / numbers.size();
    }
}

