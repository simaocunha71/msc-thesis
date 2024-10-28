        int result = 0;

        for (int i : nums) {
            if (i > 10 && isOdd(i) && isOdd(getFirstDigit(i)) && isOdd(getLastDigit(i))) {
                result += 1;
            }
        }

        return result;

    }

    private boolean isOdd(int n) {
        return n % 2 != 0;
    }

    private int getFirstDigit(int n) {
        while (n >= 10) {
            n /= 10;
        }
        return n;
    }

    private int getLastDigit(int n) {
        return n % 10;
    }
}

