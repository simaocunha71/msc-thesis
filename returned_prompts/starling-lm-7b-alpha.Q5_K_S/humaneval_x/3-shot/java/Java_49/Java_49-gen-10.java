        int result = 1;
        for (int i = 0; i < 31; i++) {
            if ((n & (1 << i)) != 0) {
                result = (result * 2) % p;
            }
        }
        return result;
    }
}

