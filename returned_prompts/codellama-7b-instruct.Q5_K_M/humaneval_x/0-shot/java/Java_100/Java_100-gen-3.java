        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            res.add(n);
            n = n % 2 == 0 ? n + 1 : n + 2;
        }
        return res;
    }
}
