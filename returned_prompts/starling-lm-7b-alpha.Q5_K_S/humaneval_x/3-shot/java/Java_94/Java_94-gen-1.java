        int max = Integer.MIN_VALUE;
        for (int i = 0; i < lst.size(); i++) {
            if (isPrime(lst.get(i)) && lst.get(i) > max) max = lst.get(i);
        }
        int sum = 0;
        while (max > 0) {
            sum += (max % 10);
            max /= 10;
        }
        return sum;
    }

    public boolean isPrime(int number) {
        if (number < 2) return false;
        for (int i = 2; i * i <= number; i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
}

