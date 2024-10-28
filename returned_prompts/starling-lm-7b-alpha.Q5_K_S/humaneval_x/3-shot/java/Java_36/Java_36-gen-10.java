        int result = 0;
        for (int i = 0; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                if (i % 10 == 7) result += 1;
            }
        }
        return result;
    }
}

