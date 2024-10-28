        double x = -xs.get(1) / xs.get(0);
        for (int i = 2; i < xs.size(); i++) {
            x -= xs.get(i) / xs.get(i - 1);
        }
        return x;
    }
}

