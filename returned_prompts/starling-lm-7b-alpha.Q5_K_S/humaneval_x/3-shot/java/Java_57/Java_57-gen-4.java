        boolean is_increasing = true;
        boolean is_decreasing = true;

        for (int i = 0; i < l.size() - 1; i++) {
            if (l.get(i) < l.get(i + 1)) {
                is_increasing = false;
            }
            if (l.get(i) > l.get(i + 1)) {
                is_decreasing = false;
            }
        }
        return is_increasing || is_decreasing;
    }
}

