        int result = 0;
        for (int i = 11; i < n; i += 11) {
            if (i % 13 == 0) result++;
        }
        for (int i = 13; i < n; i += 13) {
            if (i % 11 == 0) result++;
        }
        for (int i = 11; i < n; i += 11) {
            if (i % 13 == 0 && i % 11 == 0) result--;
        }
        return result;
    }
}

