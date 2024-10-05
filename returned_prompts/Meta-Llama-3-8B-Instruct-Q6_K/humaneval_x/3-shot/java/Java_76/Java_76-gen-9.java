        for (int i = 1; Math.pow(n, i) <= x; i++) {
            if (Math.pow(n, i) == x) {
                return true;
            }
        }
        return false;
    }
}

