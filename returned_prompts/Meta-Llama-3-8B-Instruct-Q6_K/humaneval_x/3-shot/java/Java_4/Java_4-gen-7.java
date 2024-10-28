        double mean = 0.0;
        for (double num : numbers) {
            mean += num;
        }
        mean /= numbers.size();

        double sum = 0.0;
        for (double num : numbers) {
            sum += Math.abs(num - mean);
        }
        return sum / numbers.size();
    }
}

