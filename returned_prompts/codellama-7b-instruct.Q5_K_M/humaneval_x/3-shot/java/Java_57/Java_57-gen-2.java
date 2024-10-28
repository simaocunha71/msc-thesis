        if (l.size() < 2) return true;

        boolean increasing = l.get(0) < l.get(1);
        boolean decreasing = l.get(0) > l.get(1);

        for (int i = 1; i < l.size() - 1; i++) {
            if (increasing && l.get(i) > l.get(i + 1)) return false;
            if (decreasing && l.get(i) < l.get(i + 1)) return false;
        }
        return true;
    }
}

