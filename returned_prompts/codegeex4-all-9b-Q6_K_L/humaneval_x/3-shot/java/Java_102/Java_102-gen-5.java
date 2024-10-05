        if (x > y || x % 2 != 0 || y % 2 != 0) return -1;

        if (x <= 0) x = 2;
        if (y >= 0) y = 2;

        return y;
    }
}

