        int largestPrime = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) > largestPrime) {
                largestPrime = lst.get(i);
            }
        }
        int sum = 0;
        while (largestPrime > 0) {
            sum += largestPrime % 10;
            largestPrime /= 10;
        }
        return sum;
    }
}
