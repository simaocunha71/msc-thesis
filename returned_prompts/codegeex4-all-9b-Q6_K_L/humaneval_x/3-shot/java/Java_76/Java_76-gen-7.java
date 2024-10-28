        if (x == 1) return true;
        if (n == 1) return false;
        int result = n;
        while (result < x) {
            result *= n;
        }
        return result == x;
    }
}

