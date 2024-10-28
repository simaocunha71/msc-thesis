        if (l.size() <= 1) return true;
        int direction = l.get(1) - l.get(0);
        for (int i = 2; i < l.size(); i++) {
            int current_direction = l.get(i) - l.get(i - 1);
            if (current_direction != direction) return false;
        }
        return true;
    }
}

