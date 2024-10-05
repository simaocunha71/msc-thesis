        if (xs.size() % 2 == 1 || xs.size() == 0) {
            throw new IllegalArgumentException();
        }
        double x = 0;
        for (int i = 0; i < xs.size(); i += 2) {
            x -= xs.get(i) / poly(xs.subList(i + 1, xs.size()), x);
        }
        return x;
    }
}

