        int largest_prime = -1;
        for (int i = 0; i < lst.size(); i++) {
            int number = lst.get(i);
            if (isPrime(number)) {
                largest_prime = number;
            }
        }
        return sumDigits(largest_prime);
    }

    private boolean isPrime(int number) {
        for (int i = 2; i < number; i++) {
            if (number % i == 0) return false;
        }
        return true;
    }

    private int sumDigits(int number) {
        int sum = 0;
        while (number > 0) {
            sum += number % 10;
            number /= 10;
        }
        return sum;
    }
}

