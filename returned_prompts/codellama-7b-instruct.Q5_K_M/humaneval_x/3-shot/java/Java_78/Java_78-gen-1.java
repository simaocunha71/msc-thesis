        int count = 0;
        for (char c : num.toCharArray()) {
            int digit = Character.digit(c, 16);
            if (digit != 0 && isPrime(digit)) count++;
        }
        return count;
    }

    private boolean isPrime(int number) {
        // check if number is divisible by any number between 2 and sqrt(number)
        for (int i = 2; i < Math.sqrt(number); i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
}

