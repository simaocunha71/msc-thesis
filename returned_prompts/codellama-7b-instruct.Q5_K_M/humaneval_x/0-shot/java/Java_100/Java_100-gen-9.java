        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int num = (i % 2 == 0) ? i + 1 : i + 2;
            res.add(num);
        }
        return res;
    }
}
