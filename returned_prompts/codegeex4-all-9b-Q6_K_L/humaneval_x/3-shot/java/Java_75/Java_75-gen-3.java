        int count = 0;
        for (int i = 2; i < a; i++) {
            if (a % i == 0) {
                count += 1;
                a /= i;
                i = 1;
            }
        }
        return count == 3;
    }
}

