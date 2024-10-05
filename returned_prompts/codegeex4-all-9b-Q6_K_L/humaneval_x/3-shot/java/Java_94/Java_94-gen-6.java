        int largest_prime = 2;

        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) > largest_prime) {
                if (isPrime(lst.get(i))) {
                    largest_prime = lst.get(i);
                }
            }
        }

        int sum_of_digits = 0;
        while (largest_prime > 0) {
            sum_of_digits += largest_prime % 10;
            largest_prime /= 10;
        }
        return sum_of_digits;
    }

    public boolean isPrime(int number) {
        if (number == 1) {
            return false;
        }
        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}

