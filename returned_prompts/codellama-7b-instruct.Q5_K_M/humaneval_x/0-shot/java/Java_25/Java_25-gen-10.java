        List<Integer> res = new ArrayList<Integer>();
        int i = 2;
        while (i <= n) {
            if (n % i == 0) {
                res.add(i);
                n /= i;
                continue A;
            }
            i++;
        }
        return res;
    }
}
