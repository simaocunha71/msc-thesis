        if (n < 0) return false;
        if (n % 2 != 0) return false;

        return isSumOfFourEvenNumbers(n);
    }

    private boolean isSumOfFourEvenNumbers(int n) {
        if (n == 0) return true;
        if (n % 4 != 0) return false;

        return isSumOfFourEvenNumbers(n / 4);
    }
}


```