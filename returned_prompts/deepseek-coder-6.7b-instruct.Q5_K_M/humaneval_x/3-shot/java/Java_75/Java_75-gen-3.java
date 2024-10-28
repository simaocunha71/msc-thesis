        int count = 0;
        for (int i = 2; a > 1; i++) {
            while (a % i == 0) {
                a /= i;
                count++;
            }
        }
        return count == 3;
    }
}

