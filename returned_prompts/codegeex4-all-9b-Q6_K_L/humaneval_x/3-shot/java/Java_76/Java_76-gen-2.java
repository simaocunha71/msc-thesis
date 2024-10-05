        if (x == 1) return true;
        if (x == n) return false;
        int result = n;
        while (result < x) {
            result *= n;
        }
        return result == x;
    }
}

