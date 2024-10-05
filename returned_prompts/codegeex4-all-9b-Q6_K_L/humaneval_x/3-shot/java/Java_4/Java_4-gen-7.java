        double mean = 0;
        for (double num : numbers) {
            mean += num;
        }
        mean /= numbers.size();

        double mad = 0;
        for (double num : numbers) {
            mad += Math.abs(num - mean);
        }
        mad /= numbers.size();

        return mad;
    }
}

