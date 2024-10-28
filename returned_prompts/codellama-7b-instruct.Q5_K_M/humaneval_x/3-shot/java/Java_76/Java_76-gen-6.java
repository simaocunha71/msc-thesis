        if (x < 2 || n < 2) return false;
        int i = 0;
        while (x >= 2) {
            x /= n;
            i++;
        }
        return i % 2 == 0;
    }
}

