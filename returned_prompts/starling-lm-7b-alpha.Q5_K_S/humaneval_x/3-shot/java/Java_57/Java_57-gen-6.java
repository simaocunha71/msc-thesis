        int n = l.size();
        for (int i = 1; i < n; i++) {
            if (l.get(i) > l.get(i - 1)) return false;
        }
        for (int i = 1; i < n; i++) {
            if (l.get(i) < l.get(i - 1)) return false;
        }
        return true;
    }
}

