        double sum = 0;
        double mean = 0;
        for (double number : numbers) {
            sum += Math.abs(number);
            mean += number;
        }
        return sum / numbers.size() - mean / numbers.size();
    }
}

