        List<Integer> ys = new ArrayList<>(xs.size());
        for (int i = 0; i < xs.size(); i++) {
            if (i == 0) {
                ys.add(xs.get(i));
                continue;
            }

            int a = i - 1;
            int b = i;
            int c = xs.get(a) + xs.get(b);

            ys.add(c);
        }
        return ys;
    }
}
