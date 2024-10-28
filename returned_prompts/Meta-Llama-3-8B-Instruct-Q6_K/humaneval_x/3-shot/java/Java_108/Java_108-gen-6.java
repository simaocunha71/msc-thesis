        int count = 0;
        for (int num : arr) {
            if (Math.abs(num) > 0) {
                int sumOfDigits = getSumOfDigits(Math.abs(num));
                if (sumOfDigits > 0) {
                    count++;
                }
            }
        }
        return count;
    }

    private int getSumOfDigits(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}

