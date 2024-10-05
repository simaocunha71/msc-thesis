        double sum = 0;
        double mean;
        for(double num : numbers) {
            sum += num;
        }
        mean = sum / numbers.size();

        double mad = 0;
        for(double num : numbers) {
            mad += Math.abs(num - mean);
        }
        return mad / numbers.size();
     }
}

