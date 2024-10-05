        if (x % 2 != 0) {
            x += 1;
        }
        for (int i = x; i <= y; i += 2) {
            return i;
        }
        return -1;
    }
}

