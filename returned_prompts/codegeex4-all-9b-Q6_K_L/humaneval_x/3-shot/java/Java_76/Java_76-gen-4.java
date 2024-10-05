        int result = 1;

        for (int i = 0; i < x; i++) {
            result *= n;
            if (result == x) return true;
        }
        return false;
    }
}

