        for (int i = xs.size() - 1; i > 0; i--) {
            xs.set(i, xs.get(i - 1));
        }
        xs.set(0, 1);
        return xs;
    }
}
