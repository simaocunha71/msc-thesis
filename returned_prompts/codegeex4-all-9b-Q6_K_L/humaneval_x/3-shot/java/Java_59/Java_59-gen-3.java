        int largest = 2;
        while (n > 2) {
            if (n % largest == 0) {
                n /= largest;
            } else {
                largest += 1;
            }
        }
        return largest;
    }
}

