        if (n < 0 || n == 0) return false;
        int result = 1;
        while (result < x) {
            result *= n;
        }
        return result == x;
    }
}

