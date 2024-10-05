        int result = 1;
        for (int i = 0; i < n; i++) {
            result *= 2;
            result %= p;
        }
        return result;
    }
}

