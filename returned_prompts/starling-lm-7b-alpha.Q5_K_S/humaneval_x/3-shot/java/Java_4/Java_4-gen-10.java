        double mean = 0;
        for (double number : numbers) {
            mean += number;
        }
        mean /= numbers.size();

        double mad = 0;
        for (double number : numbers) {
            mad += Math.abs(number - mean);
        }
        mad /= numbers.size();
        return mad;
    }
}

