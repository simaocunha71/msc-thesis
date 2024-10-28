        List<Integer> factors = new ArrayList<Integer>();
        int i = 2;
        while(i*i <= n) {
            if(n % i == 0) {
                while(n % i == 0) {
                    n /= i;
                }
                factors.add(i);
            } else {
                i++;
                continue A;
            }
        }
        if(n != 1) {
            factors.add(n);
        }
        return factors;
    }
}
