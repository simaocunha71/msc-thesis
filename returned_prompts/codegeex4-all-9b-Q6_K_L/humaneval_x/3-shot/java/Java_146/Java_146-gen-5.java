        int count = 0;

        for (int number : nums) {
            if (number > 10 && isOdd(number) && isOddFirstDigit(number)) {
                count += 1;
            }
        }
        return count;
    }

    private boolean isOdd(int number) {
        return number % 2 == 1;
    }

    private boolean isOddFirstDigit(int number) {
        while (number >= 10) {
            number /= 10;
        }
        return isOdd(number);
    }
}

