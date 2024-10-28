        double sum = 0;
        double mean;
        for (double num : numbers) {
            sum += num;
        }
        mean = sum / numbers.size();

        double mad = 0;
        for (double num : numbers) {
            mad += Math.abs(num - mean);
        }
        return mad / numbers.size();
    }
}

The problem with the given solution is that it does not handle the case when the list of numbers is empty. We can solve this by checking if the list is empty before proceeding with the calculation, and return 0 in such case:

