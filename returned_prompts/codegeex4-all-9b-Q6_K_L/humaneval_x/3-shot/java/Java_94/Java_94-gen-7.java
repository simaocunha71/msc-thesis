        int max = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) > max && isPrime(lst.get(i))) {
                max = lst.get(i);
            }
        }
        return sumDigits(max);
    }

    public boolean isPrime(int number) {
        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }

    public int sumDigits(int number) {
        int sum = 0;
        while (number != 0) {
            sum += number % 10;
            number = number / 10;
        }
        return sum;
    }
}

