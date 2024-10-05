        int max = 0;
        for (int i = 0; i < lst.size(); i++) {
            int temp = lst.get(i);
            if (temp != 0) {
                if (isPrime(temp)) {
                    max = temp;
                }
            }
        }

        int sum = 0;
        while (max > 0) {
            sum += max % 10;
            max /= 10;
        }
        return sum;
    }

    boolean isPrime(int number) {
        if (number <= 1) return false;
        if (number <= 3) return true;
        if (number % 2 == 0 || number % 3 == 0) return false;
        for (int i = 5; i * i <= number; i = i + 6) {
            if (number % i == 0 || number % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
}

