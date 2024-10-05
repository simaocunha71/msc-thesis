        boolean increasing = true;
        boolean decreasing = true;

        for (int i = 1; i < l.size(); i++) {
            if (l.get(i - 1) > l.get(i)) {
                increasing = false;
            }
            if (l.get(i - 1) < l.get(i)) {
                decreasing = false;
            }
        }

        return increasing || decreasing;
    }
}

