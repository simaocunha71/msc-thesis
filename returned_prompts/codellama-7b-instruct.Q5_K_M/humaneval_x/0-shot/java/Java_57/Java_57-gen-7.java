        for (int i = 0; i < l.size() - 1; i++) {
            int v = l.get(i);
            int vn = l.get(i + 1);
            if (v > vn) {
                return false;
            } else if (v < vn) {
                return true;
            }
        }
        return true;
    }
}
