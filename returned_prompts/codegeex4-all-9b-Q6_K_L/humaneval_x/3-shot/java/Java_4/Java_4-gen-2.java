        double mean = 0.0;
        for (double number : numbers) {
            mean += number;
        }
        mean /= numbers.size();

        double total = 0.0;
        for (double number : numbers) {
            total += Math.abs(number - mean);
        }
        return total / numbers.size();
    }
}

