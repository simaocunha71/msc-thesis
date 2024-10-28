        if (l.size() < 2) return true;

        int current_diff = l.get(1) - l.get(0);
        for (int i = 2; i < l.size(); i++) {
            int new_diff = l.get(i) - l.get(i - 1);
            if (current_diff * new_diff < 0) return false;
            current_diff = new_diff;
        }
        return true;
    }
}

