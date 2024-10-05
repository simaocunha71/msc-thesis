        int result = 0;
        String hex_string = "0123456789ABCDEF";
        for (char c : num.toUpperCase().toCharArray()) {
            if (hex_string.indexOf(c) != -1) {
                int digit = hex_string.indexOf(c);
                if (isPrime(digit)) result++;
            }
        }
        return result;
    }

    public boolean isPrime(int digit) {
        if (digit == 0 || digit == 1) return false;
        for (int i = 2; i <= Math.sqrt(digit); i++) {
            if (digit % i == 0) return false;
        }
        return true;
    }

}

