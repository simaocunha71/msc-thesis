        for (int i = 1; ; i++) {
            double power = Math.pow(n, i);
            if ((int) power == x) return true;
            if (power > x) return false;
        }
    }
}

