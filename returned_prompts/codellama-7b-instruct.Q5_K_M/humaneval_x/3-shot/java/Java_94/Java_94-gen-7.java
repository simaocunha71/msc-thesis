        int max_prime = -1;
        int sum = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (isPrime(lst.get(i))) {
                if (lst.get(i) > max_prime) {
                    max_prime = lst.get(i);
                    sum = 0;
                }
                sum += lst.get(i);
            }
        }
        return sum;
    }

    private boolean isPrime(int number) {
        if (number == 2) return true;
        for (int i = 2; i < number; i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
}

