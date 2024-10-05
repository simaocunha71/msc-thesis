        if (n == 0 || n == 1) {
            return new ArrayList<Integer>();
        }
        int i = 2;
        while (i <= n) {
            while (n % i == 0) {
                n /= i;
            }
            i++;
            if (n == 1) {
                break A;
            }
        }
        List<Integer> list = new ArrayList<Integer>();
        list.add(i);
        list.addAll(factorize(n));
        return list;
    }
}
