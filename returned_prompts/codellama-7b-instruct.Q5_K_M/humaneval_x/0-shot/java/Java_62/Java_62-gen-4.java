        for (int i = xs.size() - 1; i > 0; i--) {
            int tmp = 0;
            for (int j = i; j < xs.size(); j++) {
                if (j == i) {
                    tmp += xs.get(j);
                } else {
                    tmp += xs.get(j) * (j - i);
                }
            }
            xs.set(i - 1, tmp);
        }
        return xs;
    }
}
