        int result = 1;
        for (int i = 0; i < 32; i++) {
            if (((n >> i) & 1) == 1) {
                result = (result * result) % p;
            }
        }
        return result;
    }
}

