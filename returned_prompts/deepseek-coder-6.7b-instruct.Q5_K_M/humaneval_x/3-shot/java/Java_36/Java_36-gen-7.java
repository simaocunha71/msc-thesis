        int count = 0;
        for (int i = 11; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                count += countDigits(i, 7);
            }
        }
        return count;
    }

    private int countDigits(int number, int digit) {
        int count = 0;
        while (number > 0) {
            if (number % 10 == digit) {
                count++;
            }
            number = number / 10;
        }
        return count;
    }
}

