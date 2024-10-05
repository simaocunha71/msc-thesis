    public int skjkasdkd(List<Integer> lst) {
        int maxPrime = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (isPrime(lst.get(i))) {
                if (lst.get(i) > maxPrime) {
                    maxPrime = lst.get(i);
                }
            }
        }
        int sum = 0;
        while (maxPrime > 0) {
            sum += maxPrime % 10;
            maxPrime /= 10;
        }
        return sum;
    }

    public boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
