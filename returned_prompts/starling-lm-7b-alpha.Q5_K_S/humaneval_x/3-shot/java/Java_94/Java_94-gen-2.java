        int max_prime = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (is_prime(lst.get(i))) {
                max_prime = lst.get(i);
            }
        }
        return sum_of_digits(max_prime);
    }

    public boolean is_prime(int number) {
        if (number < 2) return false;
        for (int i = 2; i * i <= number; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }

    public int sum_of_digits(int number) {
        int sum = 0;
        while (number > 0) {
            sum += number % 10;
            number /= 10;
        }
        return sum;
    }
}

