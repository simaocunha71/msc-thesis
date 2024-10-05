        // The number of n-digit integers that start with 1 is 9^(n-1).
        int startWithOne = (int)Math.pow(9, n-1);
        
        // The number of n-digit integers that end with 1 is 10^(n-1) - 9^(n-1).
        int endWithOne = (int)Math.pow(10, n-1) - (int)Math.pow(9, n-1);
        
        // The total count is the sum of the two counts.
        int total = startWithOne + endWithOne;
        
        return total;
    }
}

