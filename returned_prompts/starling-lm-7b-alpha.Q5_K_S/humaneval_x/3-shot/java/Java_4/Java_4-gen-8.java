        double sum = 0.0;
        double mean = 0.0;
        for (double n : numbers) {
            sum += Math.abs(n);
            mean += n;
        }
        mean /= numbers.size();
        return sum / numbers.size() - mean;
    }
}

