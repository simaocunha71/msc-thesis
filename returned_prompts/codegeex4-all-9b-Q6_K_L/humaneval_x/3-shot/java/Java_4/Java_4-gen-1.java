        double sum = 0.0;
        double mean = 0.0;
        double mad = 0.0;

        for (double num : numbers) {
            sum += num;
        }
        mean = sum / numbers.size();
        for (double num : numbers) {
            mad += Math.abs(num - mean);
        }
        return mad / numbers.size();
    }
}

