        List<Integer> res = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            if (n % 2 == 0) {
                res.add(n + i * 2 + 1);
            } else {
                res.add(n + i * 2);
            }
        }
        return res;
    }
}

