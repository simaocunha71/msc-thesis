        boolean increasing = true;
        boolean decreasing = true;

        for (int i = 1; i < l.size(); i++) {
            int diff = l.get(i) - l.get(i - 1);
            if (diff == 0) {
                increasing = true;
                decreasing = true;
            } else if (diff > 0) {
                increasing = true;
                decreasing = false;
            } else {
                increasing = false;
                decreasing = true;
            }
        }
        return increasing || decreasing;
    }
}

