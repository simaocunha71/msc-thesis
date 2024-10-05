        int direction = 0;
        for (int i = 0; i < l.size() - 1; i++) {
            int diff = l.get(i + 1) - l.get(i);
            if (diff * direction > 0) {
                return false;
            }
            if (diff != 0) {
                direction = diff / Math.abs(diff);
            }
        }
        return true;
    }
}

