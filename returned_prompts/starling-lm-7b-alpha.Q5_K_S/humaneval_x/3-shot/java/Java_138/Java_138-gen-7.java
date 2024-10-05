        if (n % 2 == 0) {
            if (n == 2 || n == 4 || n == 6) return false;
        } else {
            if (n == 1) return true;
        }

        for (int i = 2; i < n; i += 2) {
            if (n == i + 2 + 4 + 6) return true;
        }
        return false;
    }
}

