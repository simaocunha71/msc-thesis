        if (xs.size() % 2 == 1 || Math.abs(xs.get(xs.size() - 1)) < 1e-5) return 0;
        return -xs.get(xs.size() - 1) / xs.get(xs.size() - 2);
    }
}

