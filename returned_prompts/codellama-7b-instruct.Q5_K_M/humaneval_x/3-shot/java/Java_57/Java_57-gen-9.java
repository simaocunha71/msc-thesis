        if (l.size() < 2) return true;

        int dir = l.get(1) - l.get(0);
        for (int i = 1; i < l.size() - 1; i++) {
            int d = l.get(i + 1) - l.get(i);
            if (d == 0) continue;
            if (dir * d < 0) return false;
        }
        return true;
    }
}

