        double mean = 0;
        for (double d : numbers) {
            mean += d;
        }
        mean /= numbers.size();

        double mad = 0;
        for (double d : numbers) {
            mad += Math.abs(d - mean);
        }
        mad /= numbers.size();

        return mad;
    }
}

