        List<Integer> res = new ArrayList<>();

        res.add(1);
        res.add(3);
        res.add(2);

        for (int i = 4; i <= n; i++) {
            res.add(res.get(i - 3) + res.get(i - 2) + res.get(i - 1));
        }
        return res;
    }
}





























