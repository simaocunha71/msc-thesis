        if (l.size() <= 1) return true;
        int d = l.get(1) - l.get(0);
        for (int i = 1; i < l.size() - 1; i++) {
            int dd = l.get(i + 1) - l.get(i);
            if (d * dd < 0) return false;
            d = dd;
        }
        return true;
    }
}

