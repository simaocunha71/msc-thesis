        int max_prime = 0;
        for (int i = 0; i < lst.size(); i++) {
            int current_num = lst.get(i);
            if (isPrime(current_num) && current_num > max_prime) {
                max_prime = current_num;
            }
        }
        return sumDigits(max_prime);
    }

    private int sumDigits(int num) {
        int result = 0;
        while (num > 0) {
            result += num % 10;
            num /= 10;
        }
        return result;
    }

    private boolean isPrime(int num) {
        for (int i = 2; i < num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}

