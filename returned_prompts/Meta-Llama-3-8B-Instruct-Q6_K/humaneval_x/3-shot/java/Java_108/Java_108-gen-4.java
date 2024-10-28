        int count = 0;
        for (int num : arr) {
            int sum = getSumOfDigits(Math.abs(num));
            if (sum > 0) count++;
        }
        return count;
    }

    private int getSumOfDigits(int num) {
        int sum = 0;
        while (num > 0) {
            int digit = num % 10;
            sum += digit;
            num /= 10;
        }
        return sum;
    }
}

