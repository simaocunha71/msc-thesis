        int result = 0;
        int[] primes = {2, 3, 5, 7, 11, 13};
        for (char c : num.toCharArray()) {
            int digit = Character.digit(c, 16);
            for (int prime : primes) {
                if (digit == prime) {
                    result += 1;
                    break;
                }
            }
        }
        return result;
    }
}

