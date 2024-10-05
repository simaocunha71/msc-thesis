        double base = Math.pow(n, 1);
        while (base <= x) {
            if (Math.pow(base, 1) == x) {
                return true;
            }
            base = Math.pow(base, 1) * n;
        }
        return false;
    }
}