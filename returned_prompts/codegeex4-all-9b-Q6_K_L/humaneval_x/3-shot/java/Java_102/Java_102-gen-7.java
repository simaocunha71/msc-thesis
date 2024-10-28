        if (x > y || (x % 2 != 0 && y % 2 != 0)) {
            return -1;
        }
        return Math.max(x, y) - (Math.max(x, y) % 2);
    }
}

