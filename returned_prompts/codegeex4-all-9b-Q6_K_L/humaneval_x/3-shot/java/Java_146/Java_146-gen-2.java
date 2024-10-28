        int count = 0;
        for (int n : nums) {
            if (n > 10 && isOdd(n) && isOdd(firstDigit(n)) && isOdd(lastDigit(n))) {
                count += 1;
            }
        }
        return count;
    }

    private boolean isOdd(int n) {
        return n % 2 != 0;
    }

    private int firstDigit(int n) {
        while (n >= 10) {
            n /= 10;
        }
        return n;
    }

    private int lastDigit(int n) {
        return n % 10;
    }
}

