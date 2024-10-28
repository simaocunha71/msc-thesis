        int delta = l.get(1) - l.get(0);
        for (int i = 1; i < l.size() - 1; i++) {
            int new_delta = l.get(i + 1) - l.get(i);
            if (delta * new_delta < 0) return false;
            delta = new_delta;
        }
        return true;
    }
}

