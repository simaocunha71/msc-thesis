        double y = Math.pow(n, Integer.MAX_VALUE);
        if (x < y) {
            return false;
        }
        for (int i = Integer.MAX_VALUE; i >= 0; i--) {
            if (Math.pow(n, i) == x) {
                return true;
            }
        }
        return false;
    }
}

