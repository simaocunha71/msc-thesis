        int result = 1;
        for (int i = 0; i < 32; i++) {
            result = (result << 1) % p;
            if (((1 << i) & n) != 0) {
                result = (result * 2) % p;
            }
        }
        return result;
    }
}

