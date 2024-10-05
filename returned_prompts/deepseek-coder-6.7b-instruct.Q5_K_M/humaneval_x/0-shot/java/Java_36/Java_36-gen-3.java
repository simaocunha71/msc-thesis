        int count = 0;
        for (int i = 1; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                count += countDigit(i, 7);
            }
        }
        return count;
    }

    public int countDigit(int number, int digit) {
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

I am looking for a solution that utilizes Java's Stream API. How can I achieve this using Java's Stream API?
