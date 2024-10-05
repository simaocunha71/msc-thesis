        for (int i = 2; i <= max; i += 2) {
            int b = i;
            int c = max - i;
            if (a + b + c == max) {
                return a + b + c;
            }
        }
        return -1;
    }
}

