        if (a < 2) return false;

        int count = 0;
        for (int i = 2; i <= a / 2; i++) {
            if (a % i == 0) {
                count += 1;
                a /= i;
                i = 1;
            }
        }

        return count == 3;
    }
}

