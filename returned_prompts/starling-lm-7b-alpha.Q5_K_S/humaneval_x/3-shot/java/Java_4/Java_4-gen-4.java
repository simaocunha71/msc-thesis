        double sum = 0.0;
        double mean = 0.0;
        for (double number : numbers) {
            mean += number;
        }
        mean /= numbers.size();
        for (double number : numbers) {
            sum += Math.abs(number - mean);
        }
        return sum / numbers.size();
    }
}

