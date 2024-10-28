        double mean = 0.0;
        for (Double num : numbers) {
            mean += num;
        }
        mean /= numbers.size();

        double sum = 0.0;
        for (Double num : numbers) {
            sum += Math.abs(num - mean);
        }
        return sum / numbers.size();
    }
}

